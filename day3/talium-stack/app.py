from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "talium"),
        user=os.environ.get("DB_USER", "admin"),
        password=os.environ.get("DB_PASSWORD", "secret")
    )

@app.route("/")
def home():
    return jsonify({"service": "Talium Care API", "status": "running"})

@app.route("/patients")
def get_patients():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, condition FROM patients")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {"id": r[0], "name": r[1], "condition": r[2]} for r in rows
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
