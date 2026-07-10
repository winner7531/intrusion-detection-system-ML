const qs = (selector) => document.querySelector(selector);

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}`);
  }
  return response.json();
}

async function loadStatus() {
  try {
    const health = await api("/api/health");
    qs("#apiHealth").textContent = health.status.toUpperCase();
  } catch (err) {
    qs("#apiHealth").textContent = "OFFLINE";
  }

  try {
    const model = await api("/api/model");
    qs("#modelStatus").textContent = `${model.n_features} features loaded`;
    qs("#featureCount").textContent = model.n_features;
  } catch (err) {
    qs("#modelStatus").textContent = "MODEL ERROR";
  }
}

async function submitPrediction(event) {
  event.preventDefault();
  const form = new FormData(event.target);
  const payload = { features: {} };

  for (const [key, value] of form.entries()) {
    payload.features[key] = Number(value);
  }

  qs("#predictionResult").textContent = "Running...";
  try {
    const result = await api("/api/predict", {
      method: "POST",
      body: JSON.stringify(payload),
    });
    qs("#predictionResult").textContent = JSON.stringify(result, null, 2);
  } catch (err) {
    qs("#predictionResult").textContent = `Error: ${err.message}`;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  qs("#predictForm").addEventListener("submit", submitPrediction);
  loadStatus();
});
