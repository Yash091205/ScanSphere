from pathlib import Path

PROJECT_NAME = "ScanSphere"
VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMP_DIR = BASE_DIR / "temp"

UPLOAD_DIR = TEMP_DIR / "uploads"
ENHANCED_DIR = TEMP_DIR / "enhanced"
OUTPUT_DIR = TEMP_DIR / "outputs"