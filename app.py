from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>OSSAMA-XD ULTIMATE 🔥</h1>
    <p>Version V4</p>
    <p>Status: ONLINE</p>
    """

@app.route("/api/status")
def status():
    return jsonify({
        "project": "OSSAMA-XD ULTIMATE",
        "version": "V4",
        "status": "ONLINE"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)