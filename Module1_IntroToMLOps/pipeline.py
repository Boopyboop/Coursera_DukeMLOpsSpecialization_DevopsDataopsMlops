# pipeline.py
"""Simple local MLOps pipeline orchestrator.

Steps:
 - train model (writes models/model.joblib)
 - optionally copy model into service/models (if you want to include artifact in docker build)
 - optional: build docker image (local)
 - optional: run perf test against a running instance
"""

import shutil
import subprocess
import os
from train import train_and_persist
from ops.perf_test import run_smoke_test

PROJECT = os.path.abspath(os.path.dirname(__file__))
SERVICE_MODELS = os.path.join(PROJECT, "service", "models")
LOCAL_MODEL = os.path.join(PROJECT, "models", "model.joblib")
IMAGE_TAG = os.environ.get("IMAGE_TAG", "python-devops-demo:latest")


def copy_model_to_service():
    os.makedirs(SERVICE_MODELS, exist_ok=True)
    shutil.copy2(LOCAL_MODEL, os.path.join(SERVICE_MODELS, "model.joblib"))
    print(f"Copied model to {SERVICE_MODELS}")


def build_image(tag=IMAGE_TAG):
    print(f"Building docker image {tag} (this requires Docker installed locally).")
    subprocess.check_call(["docker", "build", "-t", tag, "."])


def run_pipeline(
    build_image_flag=False, run_perf_against="http://localhost:8000/hello"
):
    print(
        "Starting pipeline: train → (copy artifact) → (optional build) → (optional perf test)"
    )
    acc = train_and_persist()
    copy_model_to_service()

    if build_image_flag:
        build_image()

    # run a simple smoke/perf test if the service is reachable
    try:
        perf_ok = run_smoke_test(run_perf_against, n_requests=20, max_avg_ms=500)
        print(f"Performance check OK: {perf_ok}")
    except Exception as e:
        print(f"Perf check failed or skipped: {e}")

    return acc


if __name__ == "__main__":
    run_pipeline(build_image_flag=False)
