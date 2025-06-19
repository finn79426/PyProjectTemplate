# Hello-World-Python

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![python_version](https://img.shields.io/badge/Python-3.13-3776AB.svg?style=flat&logo=python&logoColor=white)
[![coverage-badge](.coverage.svg)](https://pypi.org/project/coverage-badge/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

My Python Repository Template

## Features

- Automatically linting when commit changes.
- Prevent committing secrets.
- Automatically run tests when push to GitHub Repository.
- Automatically generate test coverage badge for `README.md`.

## Test

```shell=
PYTHONPATH=. uv run pytest -rA
```
