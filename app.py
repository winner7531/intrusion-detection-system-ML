import json

import joblib
import numpy as np
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow your frontend to call this from a different origin/port

# --- load model artifacts once at startup ---
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

with open("feature_names.json") as f:
    FEATURE_NAMES = json.load(f)

print(f"Model loaded. Expects {model.n_features_in_} features.")


def build_feature_vector(features_dict: dict) -> np.ndarray:
    """
    Turn a {feature_name: value} dict from the request into a properly
    ordered 1-row array matching training column order. Missing keys
    default to 0 instead of crashing, since a frontend field being
    empty shouldn't 500 the whole request.
    """
    row = [float(features_dict.get(name, 0) or 0) for name in FEATURE_NAMES]
    return np.array([row])  # shape (1, n_features) — scaler/model expect 2D

from flask import send_file

@app.route("/styles.css")
def styles():
    return send_file("styles.css")

@app.route("/app.js")
def javascript():
    return send_file("app.js")


@app.route("/")
def home():
   return send_from_directory(".", "index.html")

@app.route("/api/model", methods=["GET"])
def model_info():
    return jsonify(
        {
            "n_features": int(model.n_features_in_),
            "feature_names": FEATURE_NAMES,
            "classes": encoder.classes_.tolist(),
        }
    )


@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not data or "features" not in data:
        return jsonify({"error": "Request body must include a 'features' object"}), 400

    try:
        features = build_feature_vector(data["features"])
        scaled = scaler.transform(features)
        prediction = model.predict(scaled)
        label = encoder.inverse_transform(prediction)[0]

        # optional: include class probabilities if the model supports it
        confidence = None
        if hasattr(model, "predict_proba"):
            confidence = float(np.max(model.predict_proba(scaled)[0]))

        return jsonify({"prediction": label, "confidence": confidence})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": True
    })
if __name__ == "__main__":
    app.run(debug=True)