import subprocess
import tempfile
from pathlib import Path
from config import OUT_DIR, MODEL_FILE
from logging import verbose

def process_video(video_file: Path):
    verbose("Beginning to process '%s'" % video_file.name)
    all_detections = []
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        result = subprocess.run(
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

        verbose("ffmpeg return code: (%d)" % result.returncode)

        output_file = Path(OUT_DIR) / (video_file.stem + ".json")

        result = subprocess.run(
            [
                "python",
                "-m",
                "megadetector.detection.run_detector_batch",
                MODEL_FILE,
                str(temp_path),
                str(output_file),
                "--threshold",
                "0.8",
                "--output_relative_filenames",
                "--recursive"
            ],
            capture_output=True,
            check=True,
            text=True,
        )

        verbose("detector return code: (%d)" % result.returncode)
        verbose("stdout: <<<<<<<<<<<<")
        verbose(result.stdout)
        verbose("stderr: <<<<<<<<<<<<")
        verbose(result.stderr)
        verbose(">>>>>>>>>>>>")

    video_file.unlink()
