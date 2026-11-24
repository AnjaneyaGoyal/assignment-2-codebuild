from flask import Flask, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def index():
    return jsonify({"message": "Assignment 2 Flask Service", "status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
