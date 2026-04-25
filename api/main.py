"""Minimal FastAPI app for team workflow practice."""

from fastapi import FastAPI

app = FastAPI(title="TriageAI Practice API")


@app.get("/health")
def health():
    """Simple liveness endpoint for CI and demos."""

    return {"status": "ok"}
