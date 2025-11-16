import os
import time
from pathlib import Path
from image_processor import process_image

IN_DIR = Path("/data/in")
OUT_DIR = Path("/data/out")

def main():
    IN_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Detector started, watching /data/in ...", flush=True)

    while True:
        for img_file in IN_DIR.iterdir():
            if img_file.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp"]:
                try:
                    process_image(img_file)
                    print(f"Processed {img_file.name}", flush=True)
                except Exception as e:
                    print(f"Error processing {img_file.name}: {e}", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    main()
    