# Copilot Instructions for AI Agents

## Project Overview
This codebase is a minimal Python project located in `projectePrimer/` with a single script: `script.py`. The script currently prompts for input related to "vots dels barrufets" (votes of the Smurfs), suggesting a simple CLI utility, likely for educational or demonstration purposes.

## Key Files & Structure
- `projectePrimer/script.py`: Main Python script. All logic is currently here.
- No README or test files are present. No build system or external dependencies detected.

## Developer Workflows
- **Run the script:**
  ```zsh
  python3 projectePrimer/script.py
  ```
- **No build or test commands** are present. Add tests in a new file (e.g., `test_script.py`) if needed.

## Coding Conventions
- Simple, direct Python scripting. No classes, functions, or modules yet.
- Input/output is in Catalan. Maintain language consistency for user-facing strings.
- Expand logic in `script.py` or split into new files as the project grows.

## Patterns & Recommendations
- For new features, keep code readable and beginner-friendly.
- If adding more scripts, document their purpose in this file.
- If introducing dependencies, add a `requirements.txt` and update instructions here.
- If adding tests, use standard Python `unittest` or `pytest` and document test commands.

## Example: Adding a Feature
To add a function for calculating total votes:
```python
# ...existing code...
def calcula_total(vots):
    return sum(vots)
# ...existing code...
```

## Feedback
If any section is unclear or incomplete, please specify what needs improvement or what new patterns should be documented.
