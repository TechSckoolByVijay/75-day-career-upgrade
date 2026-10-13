# Checkpoint 1: a 2-tier app on Kubernetes, production-ready

**Week 5 (Days 29–35).** About 3–4 hours in total, spread over the week.

## The brief
Your team wants the **Notes** app ([`apps/notes-app`](../../apps/notes-app/)) running on Kubernetes. Notes is a small web app (tier 1) that stores data in **Redis** (tier 2).
The first version "works on my laptop". Your job is to make it something you'd be comfortable handing to an on-call engineer.

## Must have (acceptance criteria)
1. You built the image yourself from the Dockerfile, with a **version tag** (not `:latest`), and loaded it into kind (`kind load docker-image`).
2. Everything lives in its own **namespace**.
3. **Redis:** a Deployment plus a Service, and a **password stored in a Secret**. The password never appears in any YAML file in Git.
4. **Notes:** a Deployment with **2 replicas** plus a Service. Configuration (`APP_TITLE`, `REDIS_HOST`) comes from a **ConfigMap**, and the password from the Secret (`secretKeyRef`).
5. **Probes** on Notes: liveness → `/healthz`, readiness → `/readyz`. Know why they're different.
6. **Requests and limits** on every container.
7. **Notes survive a Redis restart:** add a **PersistentVolumeClaim** for Redis' `/data` (and start Redis with `--appendonly yes`), then prove it:
   ```bash
   # add a note in the browser, then:
   kubectl delete pod -l app=redis -n <your-namespace>
   # wait for the new pod, refresh: the note is still there
   ```
8. You can reach the app with `kubectl port-forward svc/notes 8080:80`, and the page footer says `storage: redis`.

## Also this week
- Finish the [broken Kubernetes exercises](../../exercises/broken-k8s/).
- Fill in the **Self-check** tab (the Week 5 column).

## Hand-in (to yourself)
- A public repo with `k8s/*.yaml` and a README that has a diagram (even ASCII), how to run it, and **3 things you learned**.
- A screenshot of `kubectl get pods,svc,pvc -n <ns>`.

## Score yourself
| Level | You can… |
|---|---|
| **Starter** | Get both tiers running by following docs and AI help, even if some criteria are missing |
| **Working** | Meet all 8 criteria on your own, and explain each YAML block in your own words |
| **Intermediate** | Also explain *why*: Deployment vs StatefulSet for Redis, what happens to traffic when readiness fails, what your limits protect against, and when you'd use a Job or a CronJob instead |

## Stuck?
- Read **events** first: `kubectl get events -n <ns> --sort-by=.lastTimestamp`.
- Your study-partner prompt: *"Here is my YAML and the output of kubectl describe. Don't fix it. Tell me which line of the output points to the problem."*
- Bring your question to the weekly live Q&A, or put it in the weekly check-in form.

## Optional cloud extension (Azure free account)
Run the same manifests on an AKS cluster with one small node. **Delete the cluster the same day.** Note what changed: nothing in your YAML should have to.
