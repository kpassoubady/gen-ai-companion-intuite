# Python Virtual Environments

## Why Virtual Environments?

Virtual environments isolate project dependencies, preventing conflicts between projects that need different package versions.

Without virtual environments:
- Project A needs `requests==2.28` but Project B needs `requests==2.31`
- Installing one breaks the other
- System Python gets cluttered with packages

## Creating Virtual Environments

### venv (Built-in)

```bash
# Create
python3 -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Deactivate
deactivate
```

When activated, your shell prompt changes to show the environment name: `(.venv) $`

### conda

```bash
# Create
conda create -n myproject python=3.12

# Activate
conda activate myproject

# Deactivate
conda deactivate
```

## Managing Dependencies

### pip + requirements.txt

```bash
# Install packages
pip install flask requests numpy

# Save current dependencies
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

A typical `requirements.txt`:

```
flask>=3.0.0
requests>=2.32.0
numpy>=1.26.0
python-dotenv>=1.0.0
```

### pip-tools (for pinned dependencies)

```bash
pip install pip-tools

# Create requirements.in with top-level dependencies
# Then compile to pinned requirements.txt
pip-compile requirements.in
pip-sync requirements.txt
```

## pyproject.toml

Modern Python projects use `pyproject.toml` for project metadata and dependencies:

```toml
[project]
name = "my-project"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = [
    "flask>=3.0.0",
    "requests>=2.32.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "black>=24.0.0",
]
```

Install with: `pip install -e ".[dev]"`

## Best Practices

1. Always use a virtual environment for every project
2. Never install packages into system Python
3. Include `requirements.txt` or `pyproject.toml` in version control
4. Add `.venv/` to `.gitignore`
5. Document the Python version requirement
6. Use `pip freeze` to capture exact versions for reproducibility
7. Regularly update dependencies and test for breakage
8. Use `python -m pip` instead of bare `pip` to ensure the correct Python is used
