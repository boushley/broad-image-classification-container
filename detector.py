import os
import time
import json
from pathlib import Path
from ultralytics import YOLO
import cv2

IN_DIR = Path("/data/in")
OUT_DIR = Path("/data/out")

# load a small model for speed; you can change to 'yolov8m.pt' or newer
model = YOLO("yolov8n.pt")

def process_image(img_path: Path):
    # run inference
    results = model(img_path)

    # results[0] is the first image
    r = results[0]

    # save annotated image
    annotated = r.plot()  # numpy array (BGR)
    out_img_path = OUT_DIR / f"{img_path.stem}_det.jpg"
    cv2.imwrite(str(out_img_path), annotated)

    # build json output
    detections = []
    for box in r.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        xyxy = box.xyxy[0].tolist()
        detections.append({
            "class_id": cls_id,
            "class_name": r.names[cls_id],
            "confidence": conf,
            "bbox_xyxy": xyxy,
        })

    out_json_path = OUT_DIR / f"{img_path.stem}.json"
    with out_json_path.open("w") as f:
        json.dump({
            "source_image": str(img_path.name),
            "detections": detections
        }, f, indent=2)

    # move or delete original
    img_path.unlink()  # delete after processing


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
    