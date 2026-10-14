# Week 2: Docker

**Days 8–14.** Goal for the week: *write a Dockerfile, build an image, run it with ports and environment variables, and run 2 containers together.*

**Why it matters:** containers are how modern applications are packaged and shipped, everywhere from startups to banks. Kubernetes (next week) runs containers, so this week is the foundation.
**Who can skip:** you already build and run containers at work. Do the Day 13 build anyway, with the Notes app, because you'll reuse it in Weeks 3–9.

---

## Day 8: Containers vs virtual machines (30 min)
A VM carries a whole operating system. A container shares the host's kernel and carries only your app and its libraries. That's why it starts in a second.
```bash
docker run -d -p 8080:80 --name web nginx:1.27
# open http://localhost:8080
docker ps
docker stop web && docker rm web
```

## Day 9: Look inside (30 min)
```bash
docker run -d --name web nginx:1.27
docker logs web
docker exec -it web sh       # you're now inside the container
ls /usr/share/nginx/html; exit
docker images
docker rm -f web
```
**Why:** `logs` and `exec` are the first two things you'll do when a container misbehaves, in Docker and later in Kubernetes (`kubectl logs`, `kubectl exec`).

## Day 10: Your first image (30 min)
Clone this repo and read [`apps/notes-app/Dockerfile`](../apps/notes-app/Dockerfile) **line by line**. Ask your AI study partner to explain any line you can't. Then:
```bash
cd apps/notes-app
docker build -t notes-app:1.0.0 .
docker run -p 8080:8080 notes-app:1.0.0      # open http://localhost:8080
```
Notice the tag `1.0.0`. You'll learn in Week 4 why `:latest` causes trouble.

## Day 11: Config, volumes and secrets (30 min)
```bash
docker run -p 8080:8080 -e APP_TITLE="Day 11 notes" notes-app:1.0.0
```
- **Environment variables** are how the same image behaves differently in test and production.
- **Volumes** keep data when a container is deleted.
- **`.dockerignore`** keeps files *out* of the image. Read the Notes app's `.dockerignore`: `.env` is there for a reason. A secret copied into an image is readable by anyone who can pull that image.

## Day 12: Two containers working together (30 min)
```bash
docker network create notes
docker run -d --name redis --network notes redis:7.4-alpine
docker run -p 8080:8080 --network notes -e REDIS_HOST=redis notes-app:1.0.0
```
The page footer should now say `storage: redis`. Containers on the same network find each other **by name**.
Then do the same with Docker Compose: write a `compose.yaml` with two services. Ask your AI assistant for a first draft, then check every line yourself.

## Day 13: Build day (about 60 min)
Containerise **your own** small app (your Day 6 script counts) or the Notes app, and push the image to GitHub Container Registry (`ghcr.io`).
Then ask your AI assistant: *"Review this Dockerfile for security and size problems."* Fix one thing it finds, rebuild, and compare `docker images` sizes.

## Day 14: Catch up and reflect
Weekly tab: mark the goal, and write 2 lines on what was easier or harder than expected.

## In our courses (optional)
Every task above works with the free links. If you want it faster or deeper:

| Day | Topic | Course → lecture |
|---|---|---|
| 8–9, 11–12 | Containers, images, volumes, Compose | Not in our courses yet. The Docker docs are enough. |
| 10, 13 | Writing and reviewing a Dockerfile | [ChatGPT for DevOps](https://www.readyforprod.cloud/courses/chatgpt-for-devops) → "Use ChatGPT for Generating Dockerfile" |

Next week (Kubernetes) maps to [Hands On Kubernetes](https://www.readyforprod.cloud/courses/hands-on-kubernetes).
