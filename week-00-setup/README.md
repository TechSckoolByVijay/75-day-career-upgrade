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
kind delete cluster --name upgrade
```
Stuck? Paste the **error message** (never passwords or keys) into your AI assistant and ask: *"I'm a beginner. Explain this error and how to fix it."*

## 3. Where am I today? (be honest, nobody sees this but you)
Mark each one **Yes / Somewhat / No** in your tracker:
1. I can move around folders and edit files in a Linux terminal.
2. I can clone a Git repo, commit and push a change.
3. I know what a container is and how it differs from a VM.
4. I could explain what Kubernetes does to a friend.
5. I have used a CI/CD pipeline (even just watched one run).
6. I have created something in a cloud portal (Azure, AWS or GCP).
7. I know what "infrastructure as code" means.
8. I use an AI assistant at work at least once a week.

You'll answer the same questions at the end. That's how you'll see your upgrade.

## 4. Set your goal
Write one sentence in your tracker: *"In 75 days I want to be able to ______ so that ______."*
