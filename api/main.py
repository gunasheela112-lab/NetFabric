from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from analytics.metrics import packet_loss, summarize_latency
from telemetry.ping import result_dict, run_ping

app = FastAPI(title="NetFabric API", version="0.2.0")


class PingRequest(BaseModel):
    target: str
    count: int = 5


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "netfabric-api"}


@app.get("/api/v1/metrics/summary")
def metrics_summary() -> dict:
    samples = [1.8, 2.1, 2.0, 2.4, 2.2]
    return {
        "source": "example_lab_measurement",
        "latency": summarize_latency(samples),
        "packet_loss_pct": packet_loss(100, 99),
    }


@app.post("/api/v1/measurements/ping")
def ping(request: PingRequest) -> dict:
    try:
        return result_dict(run_ping(request.target, request.count))
    except (OSError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/api/v1/metrics")
def metrics() -> dict:
    return {
        "status": "ready",
        "source": "lab",
        "note": "Metrics are collected from network experiments.",
    }


@app.get("/api/v1/experiments")
def experiments() -> list[dict[str, str]]:
    return [
        {
            "id": "link-failure",
            "name": "Controlled link failure",
            "status": "available",
        }
    ]
