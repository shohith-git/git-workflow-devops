# Git Workflow DevOps Project

## DevOps Internship - Task 4

This project demonstrates Git version control best practices by implementing a structured Git workflow. It showcases repository initialization, branch management, feature development, pull request workflow, version tagging, and project documentation using Git and GitHub.

---

## Objectives

- Initialize a Git repository
- Manage source code using Git and GitHub
- Create and work with multiple branches
- Develop features in a dedicated feature branch
- Merge changes using Pull Requests
- Use Git tags for versioning
- Document the project using Markdown
- Follow Git workflow best practices

---

## Tools Used

- Git
- GitHub
- Visual Studio Code
- Python 3

---

## Project Structure

```text
git-workflow-devops/
│
├── app/
│   └── app.py
│
├── docs/
│   ├── workflow.md
│   └── branching-strategy.md
│
├── .gitignore
└── README.md
```

---

## Git Workflow

The project follows a simple Git branching strategy.

```text
main
▲
│
feature/system-info

dev
```

### Workflow Followed

1. Initialize the Git repository.
2. Create the `main` branch.
3. Create the `dev` branch.
4. Create the `feature/system-info` branch.
5. Develop the feature.
6. Commit and push the feature branch.
7. Create a Pull Request.
8. Merge the Pull Request into the `main` branch.
9. Create and push the `v1.0` Git tag.

---

## Branches

| Branch | Purpose |
|---------|---------|
| `main` | Stable production-ready code |
| `dev` | Development branch |
| `feature/system-info` | Feature development |

---

## Git Commands Used

### Initialize Repository

```bash
git init
git branch -M main
```

### Create Branches

```bash
git checkout -b dev
git checkout -b feature/system-info
```

### Commit Changes

```bash
git add .
git commit -m "Initial project structure and documentation"

git add .
git commit -m "Add detailed system information utility"
```

### Push Changes

```bash
git push -u origin main
git push -u origin dev
git push -u origin feature/system-info
```

### Merge

The feature branch was merged into the `main` branch using a GitHub Pull Request.

### Version Tag

```bash
git tag -a v1.0 -m "Version 1.0 release"
git push origin v1.0
```

---

## Features

- Git repository initialization
- Branch management
- Feature branch workflow
- Pull Request workflow
- Git version tagging
- Markdown documentation
- Clean commit history
- Python system information utility

---

## Sample Output

```text
========================================
Git Workflow DevOps Demo
========================================
Hostname        : DESKTOP-XXXXXXX
Current User    : User
Operating System: Windows
OS Version      : 11
Machine         : AMD64
Python Version  : 3.x.x
Current Time    : YYYY-MM-DD HH:MM:SS
```

---

## Project Documentation

The project includes the following documentation:

- `README.md` – Project overview and Git workflow
- `docs/workflow.md` – Git workflow followed
- `docs/branching-strategy.md` – Branching strategy used

---

## Learning Outcomes

Through this project, the following Git concepts were practiced:

- Git repository initialization
- Git branching
- Feature branch workflow
- Pull Requests
- Merge operations
- Git version tagging
- Repository documentation
- GitHub collaboration workflow

---

## Author

**Shohith Kumar K**

- **GitHub:** https://github.com/shohith-git
- **LinkedIn:** https://www.linkedin.com/in/shohith-kumar-k-3875a2300

---

## License

This project was created as part of the **Elevate Labs DevOps Internship – Task 4**.