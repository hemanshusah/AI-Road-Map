# AI Road Map

This repository contains materials and resources for learning AI.

## Git Commands Guide

This guide will help you learn how to use Git in your terminal.

### 1. Basic Workflow (Pushing Changes)
To push your local changes to the GitHub repository, follow these steps:

1. **Check Status**: See what files have changed.
   ```bash
   git status
   ```

2. **Stage Changes**: Add the files you want to commit.
   - To add a specific file: `git add filename`
   - To add all changes: `git add .`
   ```bash
   git add .
   ```

3. **Commit**: Save your changes with a descriptive message.
   ```bash
   git commit -m "Your commit message here"
   ```

4. **Push**: Send your committed changes to the remote server (GitHub).
   ```bash
   git push origin main
   ```

### 2. Working with Branches (Making and Pushing a Branch)
Branches are useful for working on new features without affecting the main code.

1. **Create and Switch to a New Branch**:
   ```bash
   git checkout -b feature-branch-name
   ```

2. **Make your changes and Commit them**:
   ```bash
   git add .
   git commit -m "Added a new feature"
   ```

3. **Push the New Branch to GitHub**:
   Since the branch doesn't exist on GitHub yet, you need to set the "upstream" tracking:
   ```bash
   git push -u origin feature-branch-name
   ```
   *Note: After the first time, you can just use `git push`.*

### 3. Other Useful Commands
- `git pull`: Get the latest changes from GitHub to your local machine.
- `git branch`: List all local branches.
- `git log`: View the history of commits.
