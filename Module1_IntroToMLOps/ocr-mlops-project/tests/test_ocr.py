from PIL import Image, ImageDraw, ImageFont
import os
import tempfile

from src.ocr_pipeline import preprocess, ocr_image


def _create_text_image(text: str = "hello world", size=(400, 120)) -> Image.Image:
    img = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(img)
    # Try a default font; on CI we may not have system fonts, so use default bitmap.
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 48)
    except Exception:
        font = ImageFont.load_default()
    draw.text((10, 30), text, fill="black", font=font)
    return img


def test_ocr_basic_hello_world():
    img = _create_text_image("hello world")
    pre = preprocess(img, threshold=180)
    text = ocr_image(pre, lang="eng").lower()
    assert "hello" in text and "world" in text
