from pathlib import Path

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_measurement_validation():
    response = client.get("/api/v1/measurements?limit=0")
    assert response.status_code == 400


def test_missing_pcap():
    response = client.post(
        "/api/v1/analytics/pcap",
        json={"path": str(Path("missing-file.pcap"))},
    )
    assert response.status_code == 404
