# CLAUDE.md - Agent Guidelines

## Build/Test Commands
- Python unittest: `python -m unittest discover -p '*_test.py'`
- Single test: `python -m unittest test.example_test.TestStringMethods.test_upper`
- Pytest: `pytest -s test/path/to/test.py`
- Display test output: Add `-s` flag to pytest command

## Code Style Guidelines
- Python: Use type hints, follow PEP 8 guidelines
- Imports: Group standard lib, third-party, and local imports
- Markdown: No line length restrictions (MD013 disabled in markdownlint.json)
- Error handling: Use appropriate assertions in tests, try/except in production code
- Naming: Use snake_case for Python variables/functions, CamelCase for classes
- Test structure: Use unittest TestCase class with setUp/tearDown
- Mocking: Use @patch decorator or with patch() context manager for dependencies

## Repository Structure
- `/test`: Testing playground with unittest and pytest examples
- Use unittest assertions (assertEqual, assertTrue, etc.)
- Use pytest fixtures for reusable test components