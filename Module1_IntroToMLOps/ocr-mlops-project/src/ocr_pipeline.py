# pylint: disable=no-member

from __future__ import annotations
from typing import Optional
import numpy as np
from PIL import Image
import pytesseract
import cv2


def load_image(path: str) -> Image.Image:
    """Load an image from disk as a PIL Image."""
    return Image.open(path).convert("RGB")


def pil_to_cv(img: Image.Image) -> np.ndarray:
    """Convert PIL Image -> OpenCV BGR ndarray."""
    arr = np.array(img)  # RGB
    return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

def preprocess(img: Image.Image, threshold: Optional[int] = 180) -> Image.Image:
    """
    Preprocess an image for better OCR accuracy:
    - Convert to grayscale
    - Apply binary thresholding if specified
    - Return a PIL Image ready for OCR
    """
    cv_img = pil_to_cv(img)
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)  # pylint: disable=no-member

    if threshold is not None:
        _, th = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)  # pylint: disable=no-member
    else:
        th = gray

    return Image.fromarray(th)



def ocr_image(img: Image.Image, lang: str = "eng") -> str:
    """
    Run Tesseract OCR on a PIL Image.
    Requires the Tesseract binary to be installed on the system.
    """
    text = pytesseract.image_to_string(img, lang=lang)
    # Normalize whitespace
    return " ".join(text.split())


def extract_text_from_path(path: str, lang: str = "eng") -> str:
    """Convenience function: load -> preprocess -> OCR."""
    img = load_image(path)
    pre = preprocess(img)
    return ocr_image(pre, lang=lang)
