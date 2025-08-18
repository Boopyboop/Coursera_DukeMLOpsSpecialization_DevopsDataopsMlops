"""
Project configuration.
"""

import os

# Paths
DATA_DIR = os.getenv("DATA_DIR", "data")
MODEL_DIR = os.getenv("MODEL_DIR", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "text_classifier.pkl")

# ML parameters
RANDOM_STATE = 42
