@app.route("/predict_stream", methods=["POST"])
def predict_stream():
    try:
        data = request.json

        quantitative = float(data["quantitative_score"])
        verbal = float(data["verbal_score"])
        logical = float(data["logical_score"])
        creative = float(data["creative_score"])
        technical = float(data["technical_score"])

        # Improved logic using all 5 features
        if technical > 70 or quantitative > 70:
            stream = "Engineering"
        elif creative > 65:
            stream = "Arts"
        elif verbal > 60:
            stream = "Commerce"
        else:
            stream = "General"

        return jsonify({"recommended_stream": stream})

    except Exception as e:
        return jsonify({"error": str(e)})
