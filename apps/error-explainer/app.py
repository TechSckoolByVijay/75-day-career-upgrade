"""Error Explainer: the capstone app for the 75-Day Career Upgrade Challenge.

Paste an error message and get a plain-English explanation from an LLM.
The point isn't the AI. It's running an AI app like any other production
workload: config from the environment, health checks, metrics, timeouts,
and never sending secrets to a third party.

LLM_PROVIDER=fake (default) works offline and costs nothing.
LLM_PROVIDER=openai talks to any OpenAI-compatible API (OpenAI, Azure OpenAI,
or a local Ollama at http://localhost:11434/v1).
"""
import os
import re
import time

import requests
from flask import Flask, jsonify, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "fake")
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_TIMEOUT = float(os.environ.get("LLM_TIMEOUT_SECONDS", "20"))

REQUESTS = Counter("explain_requests_total", "Explain requests", ["outcome"])
LATENCY = Histogram("explain_llm_seconds", "Time spent waiting for the LLM")
REDACTIONS = Counter("explain_redactions_total", "Secrets removed before calling the LLM")

# Things that must never leave your network. Extend this list for your company.
SECRET_PATTERNS = [
    (re.compile(r"(?i)(password|passwd|pwd|secret|token|api[_-]?key)\s*[=:]\s*\S+"), r"\1=<REDACTED>"),
    (re.compile(r"(?i)bearer\s+[a-z0-9._\-]+"), "Bearer <REDACTED>"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "<REDACTED_AWS_KEY>"),
    (re.compile(r"(?i)AccountKey=[^;\s]+"), "AccountKey=<REDACTED>"),
    (re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b"), "<EMAIL>"),
]

SYSTEM_PROMPT = (
    "You help junior DevOps engineers. Explain the error in plain English in at most "
    "5 short lines: what it means, the most likely cause, and the first command to run "
    "to confirm it. If you are not sure, say so."
)


def redact(text):
    count = 0
    for pattern, replacement in SECRET_PATTERNS:
        text, n = pattern.subn(replacement, text)
        count += n
    return text, count


def ask_llm(error_text):
    if LLM_PROVIDER == "fake":
        return ("(fake LLM) This looks like an error from your tool. Read the first line, "
                "then run the matching 'describe' or 'logs' command to confirm the cause.")
    resp = requests.post(
        f"{LLM_BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {LLM_API_KEY}"},
        json={"model": LLM_MODEL, "temperature": 0.2,
              "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                           {"role": "user", "content": error_text}]},
        timeout=LLM_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()


def create_app(llm=ask_llm):
    app = Flask(__name__)

    @app.post("/explain")
    def explain():
        error_text = ((request.get_json(silent=True) or {}).get("error") or "").strip()
        if not error_text:
            REQUESTS.labels("bad_request").inc()
            return jsonify(error="send JSON like {\"error\": \"...\"}"), 400
        safe_text, removed = redact(error_text[:4000])
        REDACTIONS.inc(removed)
        start = time.perf_counter()
        try:
            answer = llm(safe_text)
        except Exception as exc:  # noqa: BLE001 - the LLM is just another dependency that can fail
            REQUESTS.labels("llm_error").inc()
            return jsonify(error=f"LLM unavailable: {type(exc).__name__}"), 502
        finally:
            LATENCY.observe(time.perf_counter() - start)
        REQUESTS.labels("ok").inc()
        return jsonify(explanation=answer, redactions=removed, provider=LLM_PROVIDER)

    @app.get("/healthz")
    def healthz():
        return jsonify(status="ok")

    @app.get("/readyz")
    def readyz():
        if LLM_PROVIDER != "fake" and not LLM_API_KEY and "localhost" not in LLM_BASE_URL:
            return jsonify(status="not ready", error="LLM_API_KEY is not set"), 503
        return jsonify(status="ready", provider=LLM_PROVIDER)

    @app.get("/metrics")
    def metrics():
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
