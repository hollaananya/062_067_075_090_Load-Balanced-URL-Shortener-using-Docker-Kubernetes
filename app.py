from flask import Flask, request, redirect, jsonify
import redis
import hashlib

app = Flask(__name__) 
# Connect to Redis (assuming Redis is running on the default port)
redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)
keys = redis_client.keys("*")
for i in keys:
    print(i +": "+ redis_client.get(i))
# Base URL for short links
BASE_URL = "http://localhost:5001/"

def generate_short_url(long_url):
    """Generate a short URL using a hash function."""
    short_code = hashlib.md5(long_url.encode()).hexdigest()[:6]  # Take first 6 chars of MD5 hash
    redis_client.set(short_code, long_url)  # Store in Redis
    return short_code

@app.route("/shorten", methods=["POST"])
def shorten_url():
    """Accept a long URL and return a shortened version."""
    data = request.get_json()
    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    short_code = generate_short_url(long_url)
    short_url = BASE_URL + short_code

    return jsonify({"short_url": short_url})

@app.route("/<short_code>")
def redirect_to_original(short_code):
    """Redirect users to the original long URL."""
    long_url = redis_client.get(short_code)

    if long_url:
        return redirect(long_url, code=302)
    else:
        return jsonify({"error": "Short URL not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
