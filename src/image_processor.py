import subprocess
from pathlib import Path
from config import MODEL_FILE
from logging import verbose
import os

def process_image(img_path: Path, output_dir: Path):
    verbose("Starting image processing for '%s':" % img_path.name)
    result = subprocess.run(
        [
            "python",
            "-m",
            "megadetector.detection.run_detector",
            MODEL_FILE,
            "--image_file",
            str(img_path),
            "--output_dir",
            str(output_dir),
            "--threshold",
            "0.8",
            "--verbose"
        ],
        capture_output=True,
        text=True,
    )

    # The detector creates a file named after the image, but we want a
    # consistent name.
    os.rename(
        output_dir / (img_path.stem + "_detections.jpg"),
        output_dir / "megadetector.json",
    )

    verbose("return code: (%d)" % result.returncode)
    verbose("stdout: <<<<<<<<<<<<")
    verbose(result.stdout)
    verbose("stderr: <<<<<<<<<<<<")
    verbose(result.stderr)
    verbose(">>>>>>>>>>>>")
