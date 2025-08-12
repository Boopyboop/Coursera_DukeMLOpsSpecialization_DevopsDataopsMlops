2
"""Small Flask microservice exposing /health, /hello and Prometheus /metrics."""

from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import joblib
import os
import time

# Import fallback logic from project (hello.py)
try:
    from hello import more_hello  # simple fallback function (exists in your project)
except Exception:
    def more_hello():
        return "hi"

app = Flask(__name__)

REQUEST_COUNT = Counter("service_request_count", "Total HTTP requests", ["endpoint"])
REQUEST_LATENCY = Histogram("service_request_latency_seconds", "Latency per endpoint", ["endpoint"])

MODEL_PATH = os.environ.get("MODEL_PATH", "/app/models/model.joblib")
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
        app.logger.info(f"Loaded model from {MODEL_PATH}")
    except Exception as e:
        app.logger.warning(f"Failed to load model at {MODEL_PATH}: {e}")


@app.route("/health")
def health():
    """Simple health endpoint."""
    return jsonify(status="ok"), 200


@app.route("/hello")
def hello():
    """Endpoint that returns model-backed output or fallback."""
    REQUEST_COUNT.labels(endpoint="hello").inc()
    start = time.time()
    with REQUEST_LATENCY.labels(endpoint="hello").time():
        if model:
            # If model exists, call its predict or a simple wrapper.
            # For a demo model we expect it to have a predict method that accepts a 2D array.
            try:
                pred = model.predict([[0] * getattr(model, "n_features_in_", 1)])
                out = str(pred[0])
            except Exception:
                out = more_hello()
        else:
            out = more_hello()
    latency_ms = round((time.time() - start) * 1000, 2)
    return jsonify(result=out, latency_ms=latency_ms), 200


@app.route("/metrics")
def metrics():
    """Prometheus metrics endpoint."""
    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
