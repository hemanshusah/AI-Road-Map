AI Road Map
This repository contains materials and resources for learning AI.

Git Commands Guide
This guide will help you learn how to use Git in your terminal.

1. Basic Workflow (Pushing Changes)
To push your local changes to the GitHub repository, follow these steps:

Check Status: See what files have changed.

git status
Stage Changes: Add the files you want to commit.

To add a specific file: git add filename
To add all changes: git add .
git add .
Commit: Save your changes with a descriptive message.

git commit -m "Your commit message here"
Push: Send your committed changes to the remote server (GitHub).

git push origin main
2. Working with Branches (Making and Pushing a Branch)
Branches are useful for working on new features without affecting the main code.

Create and Switch to a New Branch:

git checkout -b feature-branch-name
Make your changes and Commit them:

git add .
git commit -m "Added a new feature"
Push the New Branch to GitHub: Since the branch doesn't exist on GitHub yet, you need to set the "upstream" tracking:

git push -u origin feature-branch-name
Note: After the first time, you can just use git push.

3. Other Useful Commands
git pull: Get the latest changes from GitHub to your local machine.
git branch: List all local branches.
git log: View the history of commits.


Also use source .venv/bin/activate for Virtual Env

Or run uv run hello.py