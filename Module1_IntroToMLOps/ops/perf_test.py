# ops/perf_test.py
"""Simple HTTP-based smoke/perf test used in the pipeline."""

import time
import requests


def run_smoke_test(url: str, n_requests: int = 50, max_avg_ms: int = 500) -> bool:
    """Send n_requests to url and assert average latency below threshold."""
    timings = []
    successes = 0
    for i in range(n_requests):
        start = time.time()
        try:
            r = requests.get(url, timeout=5)
            latency_ms = (time.time() - start) * 1000.0
            timings.append(latency_ms)
            if r.status_code == 200:
                successes += 1
        except Exception:
            timings.append(float("inf"))

    avg_ms = sum(t for t in timings if t != float("inf")) / max(
        1, sum(1 for t in timings if t != float("inf"))
    )
    success_rate = successes / n_requests
    print(
        f"Perf summary for {url}: avg_ms={avg_ms:.1f}, success_rate={success_rate:.2%}"
    )

    if success_rate < 0.95:
        raise RuntimeError("Success rate below 95%")
    if avg_ms > max_avg_ms:
        raise RuntimeError(f"Average latency {avg_ms:.1f}ms > {max_avg_ms}ms")
    return True
