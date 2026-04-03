from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Career & Education Advisor API is running"})


@app.route("/predict_stream", methods=["POST"])
def predict_stream():
    try:
        data = request.get_json()

        # Required keys check
        required_keys = [
            "quantitative_score",
            "verbal_score",
            "logical_score",
            "creative_score",
            "technical_score",
        ]
        missing = [k for k in required_keys if k not in data]
        if missing:
            return (
                jsonify(
                    {
                        "error": "Missing keys in JSON body",
                        "missing_keys": missing,
                        "expected_format": {
                            "quantitative_score": 80,
                            "verbal_score": 60,
                            "logical_score": 70,
                            "creative_score": 50,
                            "technical_score": 46,
                        },
                    }
                ),
                400,
            )

        # Convert to float
        quantitative = float(data["quantitative_score"])
        verbal = float(data["verbal_score"])
        logical = float(data["logical_score"])
        creative = float(data["creative_score"])
        technical = float(data["technical_score"])

        # Simple rule-based logic (tu apne hisaab se tweak kar sakta hai)
        if technical > 70 or quantitative > 70:
            stream = "Engineering"
        elif creative > 65:
            stream = "Arts"
        elif verbal > 60:
            stream = "Commerce"
        else:
            stream = "General"

        # Yaha hum original scores bhi wapas bhej rahe hain "stored" form me
        return jsonify(
            {
                "input_scores": {
                    "quantitative_score": quantitative,
                    "verbal_score": verbal,
                    "logical_score": logical,
                    "creative_score": creative,
                    "technical_score": technical,
                },
                "recommended_stream": stream,
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Local testing
    app.run(host="0.0.0.0", port=5000, debug=True)
