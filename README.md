# TriageAI

This is Team 1 / Three's Company practice repo for a TriageAI MVP.

TriageAI is a small FastAPI-based practice project for learning team GitHub
workflow, basic CI with GitHub Actions, and simple API testing.

For this practice version, the goal is intentionally small:

- one FastAPI app
- one simple root endpoint for team/project info
- one health endpoint
- a small pytest suite
- one GitHub Actions workflow that runs on push

## Three's Company
![Three's Company team photo](assets/threescompany.png)

- Team: Team 1
- Team name: Three's Company
- Practice company/project: TriageAI
- Purpose: rehearse shared repo setup, testing, and CI before building a
  larger capstone MVP

## Repo Structure

```text
api/
  main.py
assets/
  threescompany.png
tests/
  test_health.py
.github/workflows/
  ci.yml
requirements.txt
README.md
```

## Local Setup

### Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run The API

### Windows

```powershell
uvicorn api.main:app --reload
```

### macOS / Linux

```bash
uvicorn api.main:app --reload
```

Then open:

- `http://127.0.0.1:8000/` for team/project info
- `http://127.0.0.1:8000/health` for the health check

Expected health response:

```json
{"status": "ok"}
```

## Run Tests

### Windows

```powershell
pytest
```

### macOS / Linux

```bash
pytest
```

## GitHub Actions

The workflow file is in `.github/workflows/ci.yml`.

It currently:

- runs on every push
- installs dependencies
- runs `pytest`

## Next Team Steps

- invite teammates as collaborators
- let each teammate work on a small feature branch
- open pull requests into `main`
- use GitHub Actions to verify pushes stay green
