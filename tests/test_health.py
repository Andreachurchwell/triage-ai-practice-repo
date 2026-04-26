from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_root_returns_team_info():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["app"] == "TriageAI"
    assert response.json()["team"] == "Team 1"
    assert response.json()["team_name"] == "Three's Company"


def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
