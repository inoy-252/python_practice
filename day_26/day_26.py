from flask import Flask, request, jsonify

# 1. Initialize the Web Application
app = Flask(__name__)

# 2. Endpoint 1: The Front Door (GET Request)
@app.route("/", methods=["GET"])
def home():
    """Health check endpoint to verify the server is running."""
    return jsonify({
        "status": "online",
        "message": "Welcome to the AI Prediction API!",
        "version": "1.0"
    })

# 3. Endpoint 2: The AI Decision Door (POST Request)
@app.route("/predict", methods=["POST"])
def predict():
    """Receives student exam scores and returns an AI evaluation."""
    # Read the incoming JSON data from the client
    incoming_data = request.get_json()

    # Safety check: did the user send data?
    if not incoming_data or "score" not in incoming_data:
        return jsonify({
            "error": "Please provide a 'score' in your JSON body."
        }), 400

    score = incoming_data["score"]

    # AI evaluation logic
    if score >= 85:
        result = "Honor Roll (High Distinction)"
    elif score >= 70:
        result = "Passed (Satisfactory)"
    else:
        result = "Needs Academic Support"

    # Send back the clean JSON answer
    return jsonify({
        "input_score": score,
        "evaluation": result,
        "status": "success"
    })

# 4. Start the Server
if __name__ == "__main__":
    print("Starting Flask API Server on http://127.0.0.1:5000 ...")
    app.run(port=5000)
