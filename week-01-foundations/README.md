# Week 1: Foundations (Linux, Git, and AI as your study partner)

**Days 1–7.** Goal for the week: *navigate and edit files in a terminal, push a commit to GitHub, and use AI to explain an error safely.*

**Why it matters:** every cloud and DevOps tool assumes you're comfortable in a terminal and with Git. Kubernetes, Terraform and pipelines are all driven from a shell, and all of them live in Git repos.
**Who can skip:** already comfortable with Linux and Git? Do only Day 5 (AI) and the Day 6 build.

On Windows, use **WSL** (Ubuntu) or **Git Bash**. Both give you a real Linux-style shell.

---

## Day 1: Move around without fear (30 min)
```bash
pwd                 # where am I?
ls -la              # what's here, including hidden files?
mkdir -p lab/day1 && cd lab/day1
touch notes.txt
cp notes.txt backup.txt
mv backup.txt old.txt
rm old.txt
cd ..  &&  cd ~     # up one level, then home
```
**Done when:** you can create, copy, move and delete files without looking at this page.
**Resource:** [Ubuntu: command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners)

## Day 2: Read and search text, like logs (30 min)
```bash
cat /etc/os-release
head -n 5 /etc/passwd
tail -n 20 /var/log/dpkg.log           # or any log file you have
grep -i error some.log | wc -l         # how many error lines?
ls -la ~ > listing.txt                 # save output to a file
history | grep git                     # what did I type before?
```
**Why:** half of troubleshooting is *finding the one line that matters* in a lot of text. `grep` and pipes (`|`) are how you do it.

## Day 3: Permissions, processes, environment (30 min)
```bash
echo 'echo hello from my script' > hello.sh
./hello.sh            # Permission denied: why?
chmod +x hello.sh && ./hello.sh
ps aux | head         # what is running?
top                   # press q to quit
export GREETING=hi && echo $GREETING
echo $PATH            # where the shell looks for commands
```
**Why:** "permission denied", "command not found" and "it works on my machine" are usually one of these three things.

## Day 4: Git, your safety net (30 min)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
mkdir my-75-days && cd my-75-days && git init
echo "# My 75 days" > README.md
git add README.md && git commit -m "Day 4: start"
git log --oneline
```
Then create an empty repo on GitHub called `my-75-days` and push to it, following GitHub's instructions. **This repo becomes your portfolio** for the next 75 days.
**Resource:** [GitHub: Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)

## Day 5: AI as your study partner, the right way (30 min)
A good question to an AI assistant has **four parts**:
1. **Context:** "I'm learning Linux on Ubuntu in WSL."
2. **What you ran:** the exact command.
3. **What happened:** the exact error, copied rather than paraphrased.
4. **What you want:** "Explain why, don't just give me the fix."

**Never paste:** passwords, keys, tokens, connection strings, customer data, internal hostnames or company code you're not allowed to share. If an error contains any of these, replace them with `<REDACTED>` first. That's a habit you'll keep for your whole career. In Week 11 you'll build an app that does it automatically.

**Try it now:** run `cat file-that-does-not-exist.txt`, and ask your AI assistant to explain the error using the four parts. Then ask: *"What are 3 other ways this could happen?"*

**Check the answer.** AI is confident even when it's wrong. Run what it suggests in your `lab` folder, never on a server you care about.

## Day 6: Build day (about 60 min)
Write `disk-report.sh` that prints:
- the disk usage of the current folder (`du -sh .`)
- the **5 largest files** below it (`find . -type f -exec du -h {} + | sort -rh | head -5`)
- today's date at the top

Make it executable, run it, commit it, and push it to your `my-75-days` repo.
Then ask your AI assistant: *"Review this script like a senior engineer. What breaks if the folder has spaces in file names, or if I run it twice?"* Apply one improvement and commit again.

## Day 7: Catch up and reflect
Finish anything from the week. In the tracker's **Weekly** tab, mark the goal and write 2 lines:
- what was easier than you expected
- what was harder

## In our courses (optional)
Every task above works with the free links. If you want it faster or deeper:

| Day | Topic | Course → lecture |
|---|---|---|
| 1–3 | Linux terminal | Not in our courses yet. The free links are enough. |
| 4 | Git and GitHub | Not in our courses yet. The free links are enough. |
| 5 | AI as your study partner | [ChatGPT for DevOps](https://www.readyforprod.cloud/courses/chatgpt-for-devops) → "Leveraging ChatGPT - Ask to Explain the Code" |
| 6 | Script + AI review | [ChatGPT for DevOps](https://www.readyforprod.cloud/courses/chatgpt-for-devops) → "Coding with ChatGPT" |
