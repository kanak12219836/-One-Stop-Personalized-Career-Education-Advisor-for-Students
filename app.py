import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load models
stream_model = joblib.load("stream_model.pkl")
admission_model = joblib.load("admission_model.pkl")

@app.route("/")
def home():
    return "ML Career Advisor API is running!"

# STREAM PREDICTION
@app.route("/predict_stream", methods=["POST"])
def predict_stream():
    try:
        data = request.json

        features = np.array([[
            float(data["quantitative_score"]),
            float(data["logical_score"]),
            float(data["verbal_score"]),
            float(data["creative_score"]),
            float(data["technical_score"])
        ]])

        prediction = stream_model.predict(features)[0]

        return jsonify({"recommended_stream": str(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})


# ADMISSION PREDICTION
@app.route("/predict_admission", methods=["POST"])
def predict_admission():
    try:
        data = request.json

        features = np.array([[
            float(data["aggregate_percentage"]),
            float(data["score_cutoff_difference"])
        ]])

        prediction = admission_model.predict(features)[0]

        return jsonify({"admission_chance": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
