"""
Model training and persistence.
"""

import os
import pickle
from sklearn.naive_bayes import MultinomialNB
from config import MODEL_PATH, MODEL_DIR

def train_model(X_train, y_train):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

def save_model(model, path=MODEL_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(model, f)

def load_model(path=MODEL_PATH):
    with open(path, "rb") as f:
        return pickle.load(f)
