"""
CLI entrypoint for the ML app.
"""

import argparse
from data import load_data, split_data, vectorize_text
from model import train_model, save_model, load_model
from predict import predict

def main():
    parser = argparse.ArgumentParser(description="Train or predict text classification.")
    parser.add_argument("--train", action="store_true", help="Train the model")
    parser.add_argument("--predict", nargs="+", help="Predict class for given texts")
    args = parser.parse_args()

    texts, labels = load_data()
    X_train_texts, X_test_texts, y_train, y_test = split_data(texts, labels)
    X_train, X_test, vectorizer = vectorize_text(X_train_texts, X_test_texts)

    if args.train:
        model = train_model(X_train, y_train)
        save_model(model)
        print("Model trained and saved.")

    if args.predict:
        model = load_model()
        preds = predict(model, vectorizer, args.predict)
        for text, pred in zip(args.predict, preds):
            print(f"{text} -> {pred}")

if __name__ == "__main__":
    main()
