# Notes: a tiny two-tier app

Flask (tier 1) + Redis (tier 2). Without `REDIS_HOST` it keeps notes in memory, so you can start with plain Python.

```bash
# 1. Plain Python
pip install -r requirements-dev.txt
pytest -q
python app.py                     # open http://localhost:8080

# 2. Docker (Week 2)
docker build -t notes-app:1.0.0 .
docker run -p 8080:8080 notes-app:1.0.0

# 3. With Redis: two containers on one network (Week 2, Day 12)
docker network create notes
docker run -d --name redis --network notes redis:7.4-alpine
docker run -p 8080:8080 --network notes -e REDIS_HOST=redis notes-app:1.0.0
```

| Endpoint | Purpose |
|---|---|
| `/` | The web page |
| `POST /notes` | Add a note (form, or JSON `{"text": "..."}`) |
| `/api/notes` | List notes as JSON |
| `/healthz` | **Liveness:** the process is alive. It never checks dependencies |
| `/readyz` | **Readiness:** it can serve traffic right now. It checks Redis |

| Env var | Default | Meaning |
|---|---|---|
| `APP_TITLE` | My Notes | Page title |
| `REDIS_HOST` | *(unset = memory)* | Redis hostname |
| `REDIS_PORT` | 6379 | Redis port |
| `REDIS_PASSWORD` | *(none)* | Redis password, from a Secret on Kubernetes |
| `APP_VERSION` | dev | Shown in the footer, so you can see which version is running |
