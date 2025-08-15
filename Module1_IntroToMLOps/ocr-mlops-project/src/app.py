import argparse
from ocr_pipeline import extract_text_from_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run OCR on an image.")
    parser.add_argument("image", help="Path to image file (png/jpg)")
    parser.add_argument("--lang", default="eng", help="Tesseract language (default: eng)")
    args = parser.parse_args()

    text = extract_text_from_path(args.image, lang=args.lang)
    print(text)


if __name__ == "__main__":
    main()
