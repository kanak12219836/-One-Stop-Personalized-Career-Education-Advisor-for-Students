from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS (frontend connect ke liye)
CORS(app)

# Home route
@app.route('/')
def home():
    return "🚀 Flask App is Running Successfully!"

# Analyze route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    quantitative = data.get("quantitative_score", 0)
    verbal = data.get("verbal_score", 0)
    logical = data.get("logical_score", 0)
    creative = data.get("creative_score", 0)
    technical = data.get("technical_score", 0)

    # Aggregate calculation
    aggregate = (quantitative + verbal + logical + creative + technical) / 5

    # Career recommendation logic
    if technical > 80 and logical > 70:
        career = "Engineering / Data Science"
    elif creative > 80:
        career = "Design / Media / Arts"
    elif verbal > 70:
        career = "Management / Law / Communication"
    else:
        career = "General Fields / Explore More"

    response = {
        "message": "Analysis Complete",
        "aggregate_percentage": aggregate,
        "recommended_career": career
    }

    return jsonify(response)

# Local run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
