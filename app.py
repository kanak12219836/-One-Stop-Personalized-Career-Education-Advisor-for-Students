from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)   # ✅ Enable CORS


# 📂 Load datasets (ensure these files are in your project folder)
colleges_df = pd.read_csv("colleges_dataset_1.csv")
students_df = pd.read_csv("_students_with_college.csv")


@app.route("/")
def home():
    return "Career & College Recommendation API Running 🚀"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # 🎯 Get input scores
        quantitative = data.get("quantitative_score", 0)
        verbal = data.get("verbal_score", 0)
        logical = data.get("logical_score", 0)
        creative = data.get("creative_score", 0)
        technical = data.get("technical_score", 0)

        # 🧮 Calculate average
        avg = (quantitative + verbal + logical + creative + technical) / 5

        # 📊 Performance label
        if avg >= 80:
            performance = "Excellent"
        elif avg >= 60:
            performance = "Good"
        elif avg >= 40:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        # 🔍 STEP 1: Find similar students (±5 range)
        similar_students = students_df[
            (students_df["avg_score"] >= avg - 5) &
            (students_df["avg_score"] <= avg + 5)
        ]

        # ❗ If no similar students found
        if similar_students.empty:
            return jsonify({
                "performance": performance,
                "average_score": avg,
                "message": "No similar students found"
            })

        # 🎓 STEP 2: Get unique colleges from similar students
        recommended_college_names = similar_students["college_name"].dropna().unique()

        # 🔍 STEP 3: Match with colleges dataset
        final_colleges = colleges_df[
            colleges_df["college_name"].isin(recommended_college_names)
        ]

        # ❗ If no colleges matched
        if final_colleges.empty:
            return jsonify({
                "performance": performance,
                "average_score": avg,
                "message": "No college recommendations found"
            })

        # 📌 STEP 4: Sort (optional: by cutoff if exists)
        if "cutoff" in final_colleges.columns:
            final_colleges = final_colleges.sort_values(by="cutoff", ascending=False)

        # 🔝 Top 5 recommendations
        top_colleges = final_colleges.head(5)

        # 📦 Convert to JSON
        recommendations = top_colleges.to_dict(orient="records")

        return jsonify({
            "performance": performance,
            "average_score": avg,
            "recommended_colleges": recommendations
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)
