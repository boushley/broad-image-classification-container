import json
import os
import subprocess
import tempfile
from pathlib import Path
from image_processor import process_image

OUT_DIR = Path("/data/out")

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

        frame_files = sorted(list(temp_path.iterdir()))
        for i, frame_file in enumerate(frame_files):
            detections = process_image(frame_file)
            all_detections.append({
                "frame_number": i,
                "frame_file": frame_file.name,
                "detections": detections
            })

    out_json_path = OUT_DIR / f"{video_file.stem}.json"
    with out_json_path.open("w") as f:
        json.dump({
            "source_video": str(video_file.name),
            "frames": all_detections
        }, f, indent=2)


    video_file.unlink()  # delete after processing
