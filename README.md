# 🌐 URI Online Judge

[![Dashboard](https://img.shields.io/badge/Dashboard-coding--challenges-blue?style=for-the-badge)](https://github.com/LorranSutter/coding-challenges) <!-- SUMMARY:START -->[![Solved Challenges](https://img.shields.io/badge/Solved%20Challenges-356-brightgreen?style=for-the-badge&logo=python&logoColor=white)](https://www.beecrowd.com.br/)<!-- SUMMARY:END -->

This repository contains my solutions for [URI Online Judge](https://www.beecrowd.com.br/) (beecrowd) problems.

URI Online Judge is a platform featuring programming challenges of various domains and difficulties to improve algorithmic thinking and problem-solving skills.

## 🛠️ Setup

No external dependencies are required. Ensure you have Python installed.

## ✨ Creating a New Problem

To create a new problem template file, run the `create_problem.sh` script:

```bash
./create_problem.sh <category> <problem_number>
```

Example:
```bash
./create_problem.sh Beginner 1001
```

Or for a tried problem (which will be excluded from the solved counts):
```bash
./create_problem.sh Tried/Beginner 1001
```

This script will validate the category and problem number, create the directories if they don't exist, check that the file doesn't already exist, and create a starter Python file with a template.

## 🔄 Updating Progress Summary

To update the progress summary table in this `README.md` after solving new problems, run the `generate_readme.py` script:

```bash
python3 generate_readme.py
```
