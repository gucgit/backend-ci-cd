from flask import Flask, jsonify

app = Flask(__name__)

# Health check / root route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "service": "backend-api",
        "message": "Flask backend running successfully"
    })

# Example API endpoint
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello from Flask API"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)