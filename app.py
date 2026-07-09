from flask import Flask, request, jsonify
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")
print(model.n_features_in_)
@app.route("/")
def home():
    return "IDS Running with model loaded"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    print("recieved data: ", data)
    #extrasct feature from json
    features = np.array(data["features"])
    print(features)
    #scale as it was in trianing
    features = scaler.transform(features)
    #predict
    prediction = model.predict(features)
    #decode the label
    label = encoder.inverse_transform(prediction)
    print(label)
    return jsonify({"prediction": label[0]})

if __name__ == "__main__":
    app.run(debug=True)