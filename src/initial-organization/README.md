# Image Organization Container

This container houses a Python script that organizes images from an input directory into a structured format, preparing them for further processing.

## Organization Process

The `organize.py` script recursively walks through the `/data/ingest` directory. For each file it finds, it performs the following actions:

1.  A new UUID (version 9) is generated for the file.
2.  The original file is copied to the `/data/assets` directory. The new filename is the generated UUID, while the original file extension is preserved.
3.  A corresponding JSON metadata file is created in the `/data/base-data` directory. The JSON filename is the UUID with a `.json` extension.

The JSON metadata file contains the following information:
-   `original_file_name`: The original name of the file.
-   `original_file_path`: The absolute path to the file within the container's filesystem (e.g., `/data/ingest/landscapes/image.jpg`).
-   `manual_classification` (optional): If a file is located in a directory structure of `.../Classified/<classification_name>/`, this field will be added to the JSON, capturing the classification name.

## Output Directories

-   `/data/assets`: This directory will contain all the original files, renamed with UUIDs.
-   `/data/base-data`: This directory will contain the JSON metadata files corresponding to each asset.

## How to Run

To run this container, you need to mount the necessary directories. The `ingest` directory should be mounted as read-only, while the `assets` and `base-data` output directories should be mounted as read-write.

Here is an example `docker run` command:

```bash
docker run --rm \
  -v /path/to/your/ingest:/data/ingest:ro \
  -v /path/to/your/assets:/data/assets:rw \
  -v /path/to/your/base-data:/data/base-data:rw \
  <your-image-name>
```

Replace `/path/to/your/ingest`, `/path/to/your/assets`, and `/path/to/your/base-data` with the absolute paths on your host machine.
