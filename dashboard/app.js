const API = window.NETFABRIC_API || "http://localhost:8000";

async function get(path, options = {}) {
  const response = await fetch(API + path, options);
  if (!response.ok) throw new Error(await response.text());
  return response.json();
}

function set(id, value) {
  document.getElementById(id).textContent = value;
}

async function loadSummary() {
  try {
    const data = await get("/api/v1/metrics/summary");
    set("mean", data.latency.mean_ms.toFixed(2) + " ms");
    set("median", data.latency.median_ms.toFixed(2) + " ms");
    set("p95", data.latency.p95_ms.toFixed(2) + " ms");
    set("latency", data.latency.p95_ms.toFixed(2));
    set("loss", data.packet_loss_pct.toFixed(2) + "%");
    set("lossDetail", data.packet_loss_pct.toFixed(2) + "%");
  } catch (error) {
    document.querySelector(".status").innerHTML = "<span></span> API OFFLINE";
  }
}

async function loadExperiments() {
  const target = document.getElementById("experiments");
  try {
    const experiments = await get("/api/v1/experiments");
    target.innerHTML = experiments.map(item =>
      '<div class="experiment"><strong>' + item.name +
      '</strong><span class="badge">' + item.status.toUpperCase() + "</span><br><small>" +
      item.id + "</small></div>"
    ).join("");
  } catch {
    target.innerHTML = "<p class='note'>API unavailable.</p>";
  }
}

document.getElementById("inspect").addEventListener("click", async () => {
  const box = document.getElementById("routeState");
  box.innerHTML = "<p>Inspecting…</p>";
  try {
    const data = await get("/api/v1/routes/inspect", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({router: "r1", destination: "10.20.20.20"})
    });
    box.innerHTML =
      '<code>Protocol: ' + (data.protocol || "unknown") +
      '<br>Next hop: ' + (data.next_hops.join(", ") || "none") +
      '<br>Interface: ' + (data.interfaces.join(", ") || "unknown") +
      '<br>Observed hops: ' + data.hop_count + "</code>";
  } catch {
    box.innerHTML = "<p class='note'>Start the API and lab to inspect live routing state.</p>";
  }
});

loadSummary();
loadExperiments();
