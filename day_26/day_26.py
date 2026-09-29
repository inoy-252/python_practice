from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "message": "My first live Python API!"})


@app.route("/predict", methods=["POST"])
def check_score():
    incoming = request.get_json()

    if not incoming or "score" not in incoming:
        return jsonify({"error": "Please provide a 'score' in your JSON body."}), 400

    user_score = incoming["score"]
    if user_score >= 80:
        evaluation = "Great job, You passed."
    else:
        evaluation = "Needs more practice."
    return jsonify({"score_recieved": user_score, "result": evaluation})


if __name__ == "__main__":
    app.run(port=5000)
