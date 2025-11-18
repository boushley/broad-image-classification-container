import subprocess
from pathlib import Path
from config import OUT_DIR, MODEL_FILE

def process_image(img_path: Path):
    print("Starting image processing for '%s':" % img_path.name)
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

    print("return code: (%d)" % result.returncode)
    print("stdout: <<<<<<<<<<<<")
    print(result.stdout)
    print("stderr: <<<<<<<<<<<<")
    print(result.stderr)
    print(">>>>>>>>>>>>")

    img_path.unlink()
