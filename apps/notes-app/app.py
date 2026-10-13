"""Notes: a tiny two-tier web app for the 75-Day Career Upgrade Challenge.

Tier 1 is this Flask app. Tier 2 is Redis, which stores the notes.
Without REDIS_HOST the app keeps notes in memory, so you can run and test
it on your laptop before you have containers or Kubernetes.
"""
import os
import socket

from flask import Flask, jsonify, redirect, render_template_string, request

APP_TITLE = os.environ.get("APP_TITLE", "My Notes")
REDIS_HOST = os.environ.get("REDIS_HOST")
# Kubernetes injects REDIS_PORT=tcp://<ip>:6379 into every pod when a Service is
# named "redis" (service links). Accept that form as well as a plain number.
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379").rsplit(":", 1)[-1])
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD") or None
VERSION = os.environ.get("APP_VERSION", "dev")

PAGE = """<!doctype html>
<title>{{ title }}</title>
<style>body{font-family:sans-serif;max-width:40rem;margin:2rem auto;padding:0 1rem}
li{margin:.3rem 0} small{color:#666}</style>
<h1>{{ title }}</h1>
<form method="post" action="/notes"><input name="text" required autofocus size="40">
<button>Add</button></form>
<ul>{% for n in notes %}<li>{{ n }}</li>{% else %}<li><i>No notes yet.</i></li>{% endfor %}</ul>
<small>version {{ version }} · served by {{ host }} · storage: {{ storage }}</small>
"""


class MemoryStore:
    def __init__(self):
        self._notes = []

    def add(self, text):
        self._notes.insert(0, text)

    def all(self):
        return list(self._notes)

    def ping(self):
        return True


class RedisStore:
    KEY = "notes"

    def __init__(self, host, port, password):
        import redis

        self._r = redis.Redis(host=host, port=port, password=password,
                              socket_connect_timeout=2, decode_responses=True)

    def add(self, text):
        self._r.lpush(self.KEY, text)

    def all(self):
        return self._r.lrange(self.KEY, 0, 99)

    def ping(self):
        return self._r.ping()


def create_app(store=None):
    app = Flask(__name__)
    if store is None:
        store = RedisStore(REDIS_HOST, REDIS_PORT, REDIS_PASSWORD) if REDIS_HOST else MemoryStore()
    storage = "redis" if isinstance(store, RedisStore) else "memory"

    @app.get("/")
    def index():
        return render_template_string(PAGE, title=APP_TITLE, notes=store.all(), version=VERSION,
                                      host=socket.gethostname(), storage=storage)

    @app.post("/notes")
    def add_note():
        text = (request.form.get("text") or (request.get_json(silent=True) or {}).get("text") or "").strip()
        if not text:
            return jsonify(error="text is required"), 400
        store.add(text[:500])
        if request.is_json:
            return jsonify(ok=True), 201
        return redirect("/")

    @app.get("/api/notes")
    def list_notes():
        return jsonify(notes=store.all())

    # Liveness: is the process alive? Never check dependencies here.
    @app.get("/healthz")
    def healthz():
        return jsonify(status="ok")

    # Readiness: can this pod serve traffic right now? Checks Redis.
    @app.get("/readyz")
    def readyz():
        try:
            store.ping()
            return jsonify(status="ready", storage=storage)
        except Exception as exc:  # noqa: BLE001 - report any storage failure
            return jsonify(status="not ready", error=str(exc)), 503

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
