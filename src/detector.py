import os
import time
from pathlib import Path
from image_processor import process_image
from video_processor import process_video
from folder_locking import FolderLock

DATA_DIR = Path("/data/")
LOCKS_DIR = DATA_DIR / "locks"

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    LOCKS_DIR.mkdir(parents=True, exist_ok=True)

    print("Detector started, watching /data/ ...", flush=True)

    while True:
        for file in DATA_DIR.iterdir():
            if not file.is_file():
                continue

            output_dir = DATA_DIR / f"{file.name}-data"

            lock_name = f"{file.name}-megadetector"
            lock = FolderLock(LOCKS_DIR, lock_name)
            if lock.acquire():
                with lock:
                    output_dir.mkdir(exist_ok=True)

                    try:
                        if file.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp"]:
                            process_image(file, output_dir)
                            print(f"Processed image {file.name}", flush=True)
                        elif file.suffix.lower() in [".mp4", ".avi", ".mov"]:
                            process_video(file, output_dir)
                            print(f"Processed video {file.name}", flush=True)
                    except Exception as e:
                        print(f"Error processing {file.name}: {e}", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    main()
