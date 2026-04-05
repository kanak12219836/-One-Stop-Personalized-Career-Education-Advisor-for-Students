from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS enable (IMPORTANT for frontend connection)
CORS(app)

# Home route
@app.route('/')
def home():
    return "🚀 Flask App is Running Successfully!"

# Analyze route
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    # Example logic (tu apna real logic yaha daal sakta hai)
    quantitative = data.get("quantitative_score", 0)
    verbal = data.get("verbal_score", 0)
    logical = data.get("logical_score", 0)
    creative = data.get("creative_score", 0)
    technical = data.get("technical_score", 0)

    # Simple calculation
    aggregate = (quantitative + verbal + logical + creative + technical) / 5

    response = {
        "message": "Data received successfully",
        "your_data": {
            "aggregate_percentage": aggregate,
            "score_cutoff_difference": 100 - aggregate
        }
    }

    return jsonify(response)

# Local run (Render ignore karega)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
