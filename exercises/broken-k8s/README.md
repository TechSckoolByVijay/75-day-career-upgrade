# Broken Kubernetes: find it, fix it

Six small manifests. Five are broken in a different way. The sixth works perfectly and still shouldn't go to production.
You'll meet every one of these problems at work. Learning to diagnose them calmly is worth more than memorising YAML.

**When:** Week 4 (Days 22–28), and again as part of Checkpoint 1.
**Time:** about 10–15 minutes each.

## Setup
```bash
kind create cluster --name upgrade      # skip if you already have one
kubectl create namespace broken
```

## How to work each one
1. `kubectl apply -f 0X-....yaml`
2. Look at what happens, **using only these commands**:
   ```bash
   kubectl -n broken get pods
   kubectl -n broken describe pod <name>        # read the Events at the bottom
   kubectl -n broken logs <name>
   kubectl -n broken get endpointslices         # which pods does a Service really reach?
   kubectl get events -n broken --sort-by=.lastTimestamp
   ```
3. Write down in your tracker notes: **the symptom, the cause, and the one line you changed.**
4. Fix the file, apply it again, and prove it works.

| # | File | Symptom you'll see |
|---|---|---|
| 1 | `01-wont-apply.yaml` | `kubectl apply` refuses it |
| 2 | `02-running-but-unreachable.yaml` | Pods are `Running` and `Ready`, but the Service reaches nothing |
| 3 | `03-never-starts.yaml` | The pod never starts |
| 4 | `04-never-ready.yaml` | `Running`, but `0/1` Ready, forever |
| 5 | `05-keeps-restarting.yaml` | Restarts again and again |
| 6 | `06-works-but-not-shippable.yaml` | Everything is green. List at least 4 reasons not to ship it |

## Using AI as your study partner (the right way)
Paste the **error or the Events section** and your YAML into ChatGPT or Claude and ask: *"Don't give me the fix yet. Which part of this output tells me what's wrong?"*
You learn to read the signals yourself. Never paste real passwords, tokens or company hostnames. The password in exercise 6 is fake.

## Clean up
```bash
kubectl delete namespace broken
```

Answers come out in the weekly email at the end of Week 4. Try first.
