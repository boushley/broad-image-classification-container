import subprocess
from pathlib import Path
from config import OUT_DIR, MODEL_FILE

def process_image(img_path: Path):
    result = subprocess.run(
        [
            "python",
            "-m",
            "megadetector.detector.run_detector",
            str(img_path),
            "--model_file",
            MODEL_FILE,
            "--output_dir",
            OUT_DIR
        ],
        capture_output=True,
        check=True,
        text=True,
    )
