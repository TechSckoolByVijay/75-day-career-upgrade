# Flawed pipeline: would you ship this?

An AI assistant wrote `deploy.yml`. It runs, and the badge is green. Your job is to review it the way a senior engineer would.

**When:** Week 9 (Checkpoint 2). **Time:** about 30 minutes.

## Your task
1. Read `deploy.yml` line by line. For every line, ask: *what happens if someone hostile can influence this?*
2. List **at least 6 problems** in your tracker notes. For each one, give:
   - the line
   - what could go wrong
   - the fix
3. Write a fixed version `deploy.fixed.yml`. Compare it with the pipeline you built for Checkpoint 2.

## Hints (open only if you're stuck)
<details><summary>Hint 1</summary>Look at <b>when</b> it runs, and <b>whose code</b> it checks out.</details>
<details><summary>Hint 2</summary>Look at what the token is allowed to do, and what gets printed to the log.</details>
<details><summary>Hint 3</summary>Which version is running in production right now? How would you roll back?</details>
<details><summary>Hint 4</summary>What has to pass before anything is deployed? And who approves a production deploy?</details>

## Study partner prompt
*"Here is a GitHub Actions workflow. Don't fix it. Ask me 5 questions, one at a time, that lead me to find its security and reliability problems myself."*

Answers come out in the weekly email at the end of Week 9.
