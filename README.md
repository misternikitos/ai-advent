# AI Advent Challenge

This repository contains solutions for the AI Advent. Each day presents a new AI-related task.

## Project Structure

The project is organized by day within the `ai_advent` package:

```
ai_advent/
└── days/
    ├── day01/
    ├── day02/
    ...
    └── day25/
```

## Getting Started

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management.

### Prerequisites

- [uv](https://github.com/astral-sh/uv) (manages Python version and dependencies)

### Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/misternikitos/ai-advent.git
    cd ai-advent
    ```

2.  **Sync dependencies:**

    This command creates the virtual environment and installs all dependencies, including development tools.

    ```bash
    uv sync
    ```

3.  **Configure environment:**

    Copy the `.env.example` file to `.env` and fill in your API keys:

    ```bash
    cp .env.example .env
    ```

4.  **Activate the virtual environment:**

    ```bash
    source .venv/bin/activate
    ```

## Development

This project uses modern Python tooling for code quality:

- [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.
- [MyPy](https://mypy-lang.org/) for static type checking.
- [Pre-commit](https://pre-commit.com/) for git hooks.

### Code Quality

To run checks manually:

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check . --fix

# Type check
uv run mypy .
```

### Pre-commit Hooks

To set up pre-commit hooks to run automatically on git commit:

```bash
uv run pre-commit install
```

## Running the Solutions

You can run the solutions using the `uv run start` command. The script supports both interactive and command-line argument modes.

### Interactive Mode

Simply run the command without arguments, and you will be prompted to enter the day number:

```bash
uv run start
# Enter day (1-25): 1
```

### Command Line Argument

You can also pass the day number directly as an argument:

```bash
uv run start 1
# Running solution for Day 1...
```

_Note: The project expects each day's folder (e.g., `ai_advent/days/day01/`) to contain a `solution.py` file._
