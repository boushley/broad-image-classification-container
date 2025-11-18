import subprocess
from pathlib import Path
from config import OUT_DIR, MODEL_FILE
from logging import verbose

def process_image(img_path: Path):
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
            OUT_DIR,
            "--threshold",
            "0.8",
            "--verbose"
        ],
        capture_output=True,
        text=True,
    )

    verbose("return code: (%d)" % result.returncode)
    verbose("stdout: <<<<<<<<<<<<")
    verbose(result.stdout)
    verbose("stderr: <<<<<<<<<<<<")
    verbose(result.stderr)
    verbose(">>>>>>>>>>>>")

    img_path.unlink()
