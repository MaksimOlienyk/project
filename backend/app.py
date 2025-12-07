from flask import Flask, jsonify
import psycopg2
import os
import redis

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port)

pg_host = os.getenv("POSTGRES_HOST", "postgres")
pg_port = int(os.getenv("POSTGRES_PORT", 5432))
pg_user = os.getenv("POSTGRES_USER", "postgres")
pg_password = os.getenv("POSTGRES_PASSWORD", "postgres")
pg_db = os.getenv("POSTGRES_DB", "postgres")

def get_pg_connection():
    return psycopg2.connect(
        host=pg_host,
        port=pg_port,
        user=pg_user,
        password=pg_password,
        database=pg_db
    )

@app.route("/test")
def test():
    r.set("test_key", "Hello Redis")
    redis_val = r.get("test_key").decode("utf-8")

    conn = get_pg_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    pg_val = cur.fetchone()[0]
    cur.close()
    conn.close()

    return jsonify({
        "message": "Backend is working!",
        "redis_test": redis_val,
        "postgres_test": pg_val
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

