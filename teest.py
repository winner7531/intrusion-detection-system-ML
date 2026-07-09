import numpy as np
import joblib

model = joblib.load("model.pkl")
label = joblib.load("label_encoder.pkl")
sample = np.zeros((1, model.n_features_in_))

prediction = model.predict(sample)
encoder = label.inverse_transform(prediction)
print(encoder)
