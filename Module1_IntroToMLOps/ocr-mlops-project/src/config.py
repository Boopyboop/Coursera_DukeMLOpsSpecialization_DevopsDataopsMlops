# config.py
"""
Configuration settings for the OCR pipeline.
"""
import os

# Absolute path to Tesseract executable
TESSERACT_CMD = os.getenv("TESSERACT_CMD", r"C:\Program Files\tesseract.exe")
