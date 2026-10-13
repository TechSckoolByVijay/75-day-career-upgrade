# Capstone: take an AI app to production

**Week 11 (Days 71–75).** About 4–6 hours.

## The brief
**Error Explainer** ([`apps/error-explainer`](../../apps/error-explainer/)) is a small AI app: send it an error message and it explains it in plain English using an LLM.
The AI part is about 20 lines. The *engineering* is what this capstone is about. To your platform, **the LLM is just another dependency**: it's slow sometimes, it fails sometimes, it costs money, and it must never receive your secrets.

**It costs nothing by default:** `LLM_PROVIDER=fake` returns a canned answer. For a real model, use a free local [Ollama](https://ollama.com/) or any OpenAI-compatible API.

## Must have (acceptance criteria)
1. **Containerised** with a version tag, and it runs as a non-root user (check the Dockerfile).
2. **Deployed to Kubernetes** with your Checkpoint 2 pipeline, reused and not rewritten.
3. **Config from the environment:** `LLM_PROVIDER`, `LLM_BASE_URL` and `LLM_MODEL` come from a ConfigMap. `LLM_API_KEY` comes from a Secret, if you use one.
4. **Secrets never reach the LLM.** Run the tests (`pytest`), then add **one redaction rule of your own** (for example your company's internal hostname pattern) with a test for it.
5. **Health:** liveness → `/healthz`, readiness → `/readyz`. Readiness fails when an API key is required but missing. Prove it.
6. **Observability:** `/metrics` exposes request counts, LLM latency and redactions. Show the numbers changing after 10 requests (`curl` it, or scrape it with Prometheus if you want to go further).
7. **Failure behaviour:** point `LLM_BASE_URL` at something that doesn't exist. The app must answer `502` quickly (timeout), not hang or crash.
8. **A one-page runbook** (`RUNBOOK.md`): what to check when users say "it's slow" or "it's broken", using your metrics, logs and probes.

## Then: pick your path
Fill in the final Self-check column and look at:
- which weeks you **enjoyed**
- where your **level** grew most

Then choose one direction to go deep for your next 75 days:
- **Kubernetes / platform engineering:** you loved weeks 3–5
- **Cloud / infrastructure as code:** weeks 7–8
- **CI/CD / DevOps automation:** weeks 6 and 9
- **AI / automation engineering:** weeks 10–11

Write **3 CV bullets** from your three projects, using verbs and specifics, for example *"Built a CI/CD pipeline that tests, builds and deploys a 2-tier app to Kubernetes on every commit, onto Terraform-managed infrastructure."*

## Score yourself
| Level | You can… |
|---|---|
| **Starter** | Run the app in Docker and on Kubernetes, with the fake provider |
| **Working** | Meet all 8 criteria |
| **Intermediate** | Also explain: what you'd add before real users (rate limiting, cost limits, caching, an audit log); why redaction belongs in the app and not just in a policy document; how you'd roll out a new model version safely |
