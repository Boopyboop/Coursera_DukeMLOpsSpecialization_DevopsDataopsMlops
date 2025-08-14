# train.py
"""Training script that uses the feature store and saves a model artifact."""

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

from feature_store import FeatureStore


MODEL_DIR = os.environ.get("MODEL_DIR", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "model.joblib")


def load_and_record_features(n_samples=1000, n_features=10, random_state=42):
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=int(n_features / 2),
        random_state=random_state,
    )
    # record simple feature statistics in the feature store
    fs = FeatureStore()
    means = {f"f{i}_mean": float(X[:, i].mean()) for i in range(X.shape[1])}
    fs.upsert("global_stats", means)
    fs.close()
    return train_test_split(X, y, test_size=0.2, random_state=random_state)


def train_and_persist():
    os.makedirs(MODEL_DIR, exist_ok=True)
    X_train, X_test, y_train, y_test = load_and_record_features()
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}; test accuracy {acc:.4f}")
    return acc


if __name__ == "__main__":
    train_and_persist()
