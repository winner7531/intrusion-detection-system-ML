import numpy as np
import requests

X_test = np.load("X_test.npy")

sample1 = X_test[0].tolist()
sample2 = X_test[1].tolist()
response = requests.post(
    "http://127.0.0.1:5000/predict",
    json={"features": [sample1, sample2]}
)

print(response.json())