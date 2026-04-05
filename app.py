from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route (IMPORTANT for Render)
@app.route('/')
def home():
    return "🚀 Flask App is Running Successfully!"

# Sample API route (tumhare project ke liye)
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    # dummy logic (baad me replace kar sakta hai)
    response = {
        "message": "Data received successfully",
        "your_data": data
    }

    return jsonify(response)

# IMPORTANT: gunicorn ke liye sirf app object chahiye hota hai
# isliye app.run() optional hai (local testing ke liye)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
