import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load dataset
df = pd.read_csv("colleges.csv")

@app.route('/')
def home():
    return "🚀 Flask App is Running Successfully!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    quantitative = data.get("quantitative_score", 0)
    verbal = data.get("verbal_score", 0)
    logical = data.get("logical_score", 0)
    creative = data.get("creative_score", 0)
    technical = data.get("technical_score", 0)

    aggregate = (quantitative + verbal + logical + creative + technical) / 5

    # Career logic
    if technical > 80 and logical > 70:
        career = "Engineering"
        filtered = df[df["stream"] == "Engineering"]

    elif creative > 80:
        career = "Design"
        filtered = df[df["stream"] == "Design"]

    elif verbal > 70:
        career = "Management"
        filtered = df[df["stream"] == "Management"]

    else:
        career = "General"
        filtered = df

    # Filter by cutoff
    recommended = filtered[filtered["cutoff"] <= aggregate]

    # Top 5 colleges
    colleges = recommended["college_name"].head(5).tolist()

    response = {
        "message": "Analysis Complete",
        "aggregate_percentage": aggregate,
        "recommended_career": career,
        "recommended_colleges": colleges
    }

    return jsonify(response)
