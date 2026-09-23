from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from analytics.metrics import packet_loss, summarize_latency
from analytics.path import hop_count
from analytics.pcap_reader import summarize_pcap
from analytics.timeseries import experiment_summary, group_metric_series
from storage.store import recent, record
from telemetry.ping import result_dict, run_ping
from telemetry.routes import inspect_route

app = FastAPI(title="NetFabric API", version="0.5.0")


class PingRequest(BaseModel):
    target: str
    count: int = 5
    experiment_id: str = "ad-hoc-ping"


class RouteRequest(BaseModel):
    router: str
    destination: str


class MeasurementRequest(BaseModel):
    experiment_id: str
    metric: str
    value: float
    unit: str
    source: str
    target: str | None = None


class PcapRequest(BaseModel):
    path: str


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
        result = run_ping(request.target, request.count)
        record(request.experiment_id, "latency_avg", result.avg_ms or 0.0,
               "ms", "icmp", request.target)
        record(request.experiment_id, "packet_loss", result.loss_pct,
               "percent", "icmp", request.target)
        return result_dict(result)
    except (OSError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/v1/routes/inspect")
def route_inspect(request: RouteRequest) -> dict:
    if not request.router or not request.destination:
        raise HTTPException(status_code=400, detail="router and destination are required")
    result = inspect_route(request.router, request.destination)
    return {
        "router": result.router,
        "destination": result.destination,
        "protocol": result.protocol,
        "next_hops": result.next_hops,
        "interfaces": result.interfaces,
        "hop_count": hop_count(result.next_hops),
    }


@app.post("/api/v1/measurements")
def add_measurement(request: MeasurementRequest) -> dict:
    record(request.experiment_id, request.metric, request.value,
           request.unit, request.source, request.target)
    return {"status": "recorded"}


@app.get("/api/v1/measurements")
def measurements(experiment_id: str | None = None, limit: int = 100) -> list[dict]:
    return recent(experiment_id, limit)


@app.get("/api/v1/analytics/series")
def series(metric: str = "latency_avg", limit: int = 500) -> dict:
    rows = recent(limit=limit)
    return {"metric": metric, "series": group_metric_series(rows, metric)}


@app.get("/api/v1/analytics/experiments")
def experiment_comparison(limit: int = 500) -> list[dict]:
    return experiment_summary(recent(limit=limit))


@app.post("/api/v1/analytics/pcap")
def pcap_analysis(request: PcapRequest) -> dict:
    try:
        return summarize_pcap(request.path)
    except (OSError, RuntimeError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/api/v1/metrics")
def metrics() -> dict:
    return {"status": "ready", "source": "lab", "storage": "sqlite"}


@app.get("/api/v1/experiments")
def experiments() -> list[dict[str, str]]:
    return [
        {"id": "link-failure", "name": "Controlled link failure", "status": "available"},
        {"id": "convergence", "name": "Route convergence", "status": "available"},
    ]
