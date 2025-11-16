import os
import time
from pathlib import Path
from image_processor import process_image
from video_processor import process_video

IN_DIR = Path("/data/in")
OUT_DIR = Path("/data/out")

def main():
    IN_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Detector started, watching /data/in ...", flush=True)

    while True:
        for file in IN_DIR.iterdir():
            try:
                if file.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp"]:
                    process_image(file)
                    print(f"Processed image {file.name}", flush=True)
                elif file.suffix.lower() in [".mp4", ".avi", ".mov"]:
                    process_video(file)
                    print(f"Processed video {file.name}", flush=True)
            except Exception as e:
                print(f"Error processing {file.name}: {e}", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    main()
