from flask import Flask, jsonify

app = Flask(__name__)

patients = [
    {"id": 1, "name": "John Adeyemi", "condition": "Diabetes"},
    {"id": 2, "name": "Mary Okafor", "condition": "Hypertension"},
]

@app.route("/")
def home():
    return jsonify({"service": "Talium Care API", "status": "running"})

@app.route("/patients")
def get_patients():
    return jsonify(patients)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
