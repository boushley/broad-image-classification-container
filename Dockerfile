# Base: CUDA + cuDNN + Ubuntu
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04

# Avoid tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

# Ensure NVIDIA libraries are found
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib64:$LD_LIBRARY_PATH

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    git \
    ffmpeg \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Make python3 the default "python"
RUN ln -s /usr/bin/python3 /usr/bin/python

# Create and activate venv
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Upgrade pip
RUN python -m pip install --upgrade pip

# ----- PYTHON PACKAGES -----
# 1) Install torch/torchvision/torchaudio with CUDA wheels
# Adjust the versions if you need a specific torch version,
# but this index URL is the usual way to get CUDA-enabled wheels.
RUN pip install --no-cache-dir \
    torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 2) Install ultralytics and opencv
RUN pip install --no-cache-dir \
    ultralytics==8.3.0 \
    opencv-python==4.10.0.84

# Copy your detector script (same as the CPU version)
COPY detector.py /app/detector.py

# Create data dirs
RUN mkdir -p /data/in /data/out

# Default command
CMD ["python", "/app/detector.py"]
