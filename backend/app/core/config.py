from pathlib import Path

# ---------------------------------------------------
# Project Information
# ---------------------------------------------------

PROJECT_NAME = "ScanSphere"
VERSION = "1.0.0"

# ---------------------------------------------------
# Base Directories
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMP_DIR = BASE_DIR / "temp"

UPLOAD_DIR = TEMP_DIR / "uploads"
SCANNED_DIR = TEMP_DIR / "scanned"
ENHANCED_DIR = TEMP_DIR / "enhanced"
OCR_DIR = TEMP_DIR / "ocr"
OUTPUT_DIR = TEMP_DIR / "outputs"

# ---------------------------------------------------
# Upload Limits
# ---------------------------------------------------

MAX_FILE_SIZE_MB = 50
MAX_PAGE_LIMIT = 30

# ---------------------------------------------------
# OCR
# ---------------------------------------------------

SUPPORTED_LANGUAGES = [
    "eng",
    "hin",
    "mar"
]