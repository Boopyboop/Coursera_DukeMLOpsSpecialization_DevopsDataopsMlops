"""
Data loading and preprocessing.
"""

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

def load_data():
    """
    Dummy dataset: list of texts and labels.
    Replace with real dataset in production.
    """
    texts = ["I love this", "I hate that", "This is amazing", "This is terrible"]
    labels = ["positive", "negative", "positive", "negative"]
    return texts, labels

def split_data(texts, labels, test_size=0.25):
    return train_test_split(texts, labels, test_size=test_size, random_state=42)

def vectorize_text(train_texts, test_texts):
    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(train_texts)
    X_test = vectorizer.transform(test_texts)
    return X_train, X_test, vectorizer
