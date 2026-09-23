# NetFabric Operations Console

A lightweight operator-facing dashboard for the NetFabric lab.

## Run

Start the API:

```bash
uvicorn api.main:app --reload
```

Serve the dashboard directory with any static HTTP server:

```bash
python -m http.server 8080 --directory dashboard
```

Open the dashboard at `http://localhost:8080`.

The browser calls the FastAPI service at `http://localhost:8000` by default. Set `window.NETFABRIC_API` before loading `app.js` if the API is hosted elsewhere.

## Design

The dashboard deliberately does not own network state. It requests route and measurement data from the API, which in turn reads the lab/measurement layer.

Panels cover:

- topology
- routing state
- latency and packet loss
- experiment status

The next UI iteration can add historical charts once persistent experiment storage is introduced.
