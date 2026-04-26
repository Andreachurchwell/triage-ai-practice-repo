"""Minimal FastAPI app for team workflow practice."""

from fastapi import FastAPI

app = FastAPI(title="TriageAI Practice API")


@app.get("/")
def root():
    """Small homepage endpoint for demos and sanity checks."""

    return {
        "app": "TriageAI",
        "team": "Team 1",
        "team_name": "Three's Company",
        "message": "TriageAI practice repo is running.",
    }


@app.get("/health")
def health():
    """Simple liveness endpoint for CI and demos."""

    return {"status": "ok"}
