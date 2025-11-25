import os
import json
import shutil
from uuid_v9 import uuid9

# Define the source and destination directories
ingest_dir = "/data/ingest"
assets_dir = "/data/assets"
base_data_dir = "/data/base-data"

# Create the destination directories if they don't exist
os.makedirs(assets_dir, exist_ok=True)
os.makedirs(base_data_dir, exist_ok=True)

# Walk through the ingest directory
for root, _, files in os.walk(ingest_dir):
    for filename in files:
        # Get the original file path
        original_file_path = os.path.join(root, filename)

        # Generate a UUID v9
        new_uuid = uuid9()

        # Get the file extension
        _, extension = os.path.splitext(filename)

        # Construct the new asset file path
        asset_filename = f"{new_uuid}{extension}"
        asset_filepath = os.path.join(assets_dir, asset_filename)

        # Construct the new JSON file path
        json_filename = f"{new_uuid}.json"
        json_filepath = os.path.join(base_data_dir, json_filename)

        # Create the JSON data
        json_data = {
            "original_file_name": filename,
            "original_file_path": original_file_path,
        }

        # Check for manual_classification
        parent_dir = os.path.basename(root)
        grandparent_dir = os.path.basename(os.path.dirname(root))
        if grandparent_dir == "Classified":
            json_data["manual_classification"] = parent_dir

        # Copy the file to the assets directory
        shutil.copy(original_file_path, asset_filepath)

        # Write the JSON data to the base-data directory
        with open(json_filepath, "w") as f:
            json.dump(json_data, f, indent=4)

print("Data organization complete.")
