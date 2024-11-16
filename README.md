# Matrix Processing

[![GH_Build Icon]][GH_Build Status]&emsp;[![License Icon]][LICENSE]

[GH_Build Icon]: https://img.shields.io/github/actions/workflow/status/1git2clone/matrix-processing/ci.yml?branch=main
[GH_Build Status]: https://github.com/1git2clone/currency-conversion/actions?query=branch%3Amain
[License Icon]: https://img.shields.io/badge/license-MIT-blue.svg
[LICENSE]: LICENSE

A simple matrix processing project for operations like:

- Inversion
- Equality checks

## Setting up

This guide shows how to set the project up with
[uv](https://docs.astral.sh/uv/getting-started/installation/ "docs.astral.sh/uv/getting-started/installation/").

### On Linux/MacOS

```sh
uv venv
source ./.venv/bin/activate # On windows: `.venv\Scripts\activate`
uv pip install -r requirements.txt
uv run ./src/main.py
```

### On Windows

```powershell
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
uv run .\src\main.py
```
