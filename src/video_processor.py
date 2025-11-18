import subprocess
import tempfile
from pathlib import Path
from config import OUT_DIR, MODEL_FILE

def process_video(video_file: Path):
    all_detections = []
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                str(video_file),
                "-vf",
                "fps=1",
                str(temp_path / "frame_%04d.png"),
            ],
            check=True,
            capture_output=True,
        )

        result = subprocess.run(
            [
                "python",
                "-m",
                "megadetector.detector.run_detector_batch",
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

    video_file.unlink()  # delete after processing
