from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_experiments():
    response = client.get("/api/v1/experiments")
    assert response.status_code == 200
    assert response.json()[0]["id"] == "link-failure"
