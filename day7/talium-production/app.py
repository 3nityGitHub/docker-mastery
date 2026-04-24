from flask import Flask, jsonify
import psycopg2
import redis
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "talium"),
        user=os.environ.get("DB_USER", "admin"),
        password=os.environ.get("DB_PASSWORD", "secret")
    )

def get_cache():
    return redis.Redis(
        host=os.environ.get("REDIS_HOST", "redis"),
        port=6379,
        decode_responses=True
    )

@app.route("/")
def home():
    return jsonify({"service": "Talium Care API", "status": "running", "version": "3.0"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/patients")
def get_patients():
    cache = get_cache()
    cached = cache.get("patients")
    if cached:
        return jsonify({"source": "cache", "data": cached})
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, condition FROM patients")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    patients = [{"id": r[0], "name": r[1], "condition": r[2]} for r in rows]
    cache.set("patients", str(patients), ex=60)
    return jsonify({"source": "database", "data": patients})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
