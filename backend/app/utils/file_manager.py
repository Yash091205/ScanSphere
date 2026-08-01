import shutil
from pathlib import Path


def ensure_directory(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def save_file(source, destination: Path):
    with destination.open("wb") as buffer:
        shutil.copyfileobj(source, buffer)