import os
import subprocess
import tempfile
from pathlib import Path
from image_processor import process_image

def process_video(video_file: Path):
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
        for frame_file in temp_path.iterdir():
            process_image(frame_file)

    video_file.unlink()  # delete after processing
