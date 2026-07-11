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

function readFileAsJson(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      try {
        resolve(JSON.parse(reader.result));
      } catch (err) {
        reject(new Error("File is not valid JSON"));
      }
    };
    reader.onerror = () => reject(new Error("Could not read file"));
    reader.readAsText(file);
  });
}

async function submitPrediction(event) {
  event.preventDefault();
  const fileInput = qs("#featureFile");
  const file = fileInput.files[0];

  if (!file) {
    qs("#predictionResult").textContent = "Error: choose a JSON file first.";
    return;
  }

  qs("#predictionResult").textContent = "Running...";
  try {
    const features = await readFileAsJson(file);
    const result = await api("/api/predict", {
      method: "POST",
      body: JSON.stringify({ features }),
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