from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict_stream", methods=["POST"])
def predict_stream():
    try:
        data = request.json

        quantitative = float(data["quantitative_score"])
        verbal = float(data["verbal_score"])
        logical = float(data["logical_score"])

        if quantitative > 70:
            stream = "Engineering"
        elif verbal > 70:
            stream = "Arts"
        else:
            stream = "Commerce"

        return jsonify({"recommended_stream": stream})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/predict_admission", methods=["POST"])
def predict_admission():
    try:
        data = request.json

        percentage = float(data["aggregate_percentage"])
        cutoff_diff = float(data["score_cutoff_difference"])

        if percentage >= 75 and cutoff_diff <= 5:
            result = "High Chance"
        else:
            result = "Low Chance"

        return jsonify({"admission_prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/")
def home():
    return "API is running!"
