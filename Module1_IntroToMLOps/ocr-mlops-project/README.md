# ocr_ops

Minimal OCR pipeline with CI:
- Preprocess (grayscale + threshold) and OCR via Tesseract (`pytesseract`)
- CLI: `python -m src.app path/to/image.jpg`
- Unit test that generates an image and verifies OCR
- CI installs `tesseract-ocr` and runs tests on every push/PR

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
make all
