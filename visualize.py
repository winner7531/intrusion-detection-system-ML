# visualize.py
import numpy as np
import matplotlib.pyplot as plt
import joblib
import json

# load model and feature names
model = joblib.load("model.pkl")
feature_names = json.load(open("feature_names.json"))

# feature importance
importances = model.feature_importances_
idx = np.argsort(importances)[::-1][:20]  # top 20 indices

plt.figure(figsize=(12, 6))
plt.bar(range(20), importances[idx], color="#3b82f6")
plt.xticks(range(20), [feature_names[i] for i in idx], rotation=45, ha="right")
plt.title("Top 20 Feature Importances — IDS Random Forest")
plt.xlabel("Feature")
plt.ylabel("Importance Score")
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=150)
print("Saved feature_importance.png")