# Error Explainer: a small AI app, run like production

```bash
pip install -r requirements-dev.txt
pytest -q                          # includes "secrets never reach the LLM"
python app.py
curl -X POST localhost:8080/explain -H 'content-type: application/json' \
     -d '{"error": "Back-off pulling image \"redis:7.4-alpnie\""}'
```

| Env var | Default | Meaning |
|---|---|---|
| `LLM_PROVIDER` | `fake` | `fake` (free, offline) or `openai` (any OpenAI-compatible API) |
| `LLM_BASE_URL` | `https://api.openai.com/v1` | For a local Ollama: `http://localhost:11434/v1` |
| `LLM_MODEL` | `gpt-4o-mini` | For Ollama, for example `llama3.2` |
| `LLM_API_KEY` | *(none)* | From a Secret. Never in Git |
| `LLM_TIMEOUT_SECONDS` | 20 | The LLM is a dependency. Don't wait forever |

Endpoints: `POST /explain`, `/healthz`, `/readyz`, `/metrics` (Prometheus format).
