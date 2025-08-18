"""
Prediction wrapper.
"""

from model import load_model
from data import vectorize_text

def predict(model, vectorizer, texts):
    X_test = vectorizer.transform(texts)
    return model.predict(X_test)
