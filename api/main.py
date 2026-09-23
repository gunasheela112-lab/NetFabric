from fastapi import FastAPI

from analytics.metrics import packet_loss, summarize_latency

app = FastAPI(title="NetFabric API", version="0.1.0")


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


@app.get("/api/v1/metrics")
def metrics() -> dict:
    return {
        "status": "ready",
        "source": "lab",
        "note": "Live collectors are introduced in the telemetry milestone.",
    }


@app.get("/api/v1/experiments")
def experiments() -> list[dict[str, str]]:
    return [
        {
            "id": "link-failure",
            "name": "Controlled link failure",
            "status": "planned",
        }
    ]
