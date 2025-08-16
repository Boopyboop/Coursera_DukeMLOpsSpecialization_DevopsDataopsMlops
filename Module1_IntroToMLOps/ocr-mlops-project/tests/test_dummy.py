"""
Tests OCR pipeline on a generated dummy image with text.
"""

import os
from PIL import Image, ImageDraw
from src.ocr_pipeline import extract_text_from_path


def create_dummy_image(path: str, text: str = "Hello World") -> None:
    """Generate a dummy image with given text and save to `path`."""
    img = Image.new("RGB", (200, 100), color="white")
    draw = ImageDraw.Draw(img)
    draw.text((10, 40), text, fill="black")
    img.save(path)


def test_dummy_image(tmp_path):
    """Test OCR pipeline on a generated dummy image."""
    dummy_path = tmp_path / "dummy.png"
    create_dummy_image(dummy_path)

    result = extract_text_from_path(str(dummy_path), lang="eng")

    # Normalize OCR output (case-insensitive, strip whitespace)
    assert "hello" in result.lower()
    assert "world" in result.lower()
