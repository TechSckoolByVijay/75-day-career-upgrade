# Week 0: Setup and "where am I today?"

Do this any time before your Day 1. It takes about 60–90 minutes in total.

## 1. Install
- [ ] **Git**: https://git-scm.com/downloads
- [ ] **VS Code**: https://code.visualstudio.com/
- [ ] **Docker Desktop**: https://www.docker.com/products/docker-desktop/ (on Windows, enable WSL 2 when asked)
- [ ] **kubectl**: https://kubernetes.io/docs/tasks/tools/
- [ ] **kind** (Kubernetes in Docker): https://kind.sigs.k8s.io/docs/user/quick-start/#installation
- [ ] A free **GitHub** account
- [ ] A free **ChatGPT** or **Claude** account, your study partner for 75 days

## 2. Check it works
```bash
git --version
docker run hello-world
kubectl version --client
kind create cluster --name upgrade
kubectl get nodes          # one node, STATUS Ready
kind delete cluster --name upgrade   # or keep it: you'll use it from Week 3
```
Stuck? Paste the **error message** (never passwords or keys) into your AI assistant and ask: *"I'm a beginner. Explain this error and how to fix it."*

## 3. Where am I today? (be honest, nobody sees this but you)
In the tracker's **Self-check** tab, mark each one **Yes / Somewhat / No** in the *Start* column. *Can I…*
1. move around folders and edit files in a Linux terminal?
2. clone a Git repo, commit and push a change?
3. explain what a container is and how it differs from a VM?
4. explain what Kubernetes does, to a friend?
5. deploy an app built from a Dockerfile to Kubernetes?
6. explain when to use a Job, a CronJob or a Deployment?
7. use a PersistentVolumeClaim comfortably?
8. say why a Kubernetes YAML is NOT production-ready (probes, limits, secrets, image tags)?
9. build a CI/CD pipeline that builds and tests on every push?
10. create something in a cloud and clean it up again?
11. explain what infrastructure as code means, and use Terraform plan/apply?
12. use an AI assistant at work safely, at least once a week?

Most people start with 0–3 Yes. That's the point. You'll answer the same questions in weeks 5, 9 and 11 and watch your level change: **Starter** (0–4) → **Working** (5–8) → **Intermediate** (9–12).

## 4. Set your goal
Write one sentence in your tracker: *"In 75 days I want to be able to ______ so that ______."*
