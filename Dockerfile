FROM zaandahl/mewc-detect:6.0
# Workdir
WORKDIR /app

RUN mv /code/md_v1000.0.0-redwood.pt /app/md_v1000.0.0-redwood.pt
RUN rm -rf /code

# Copy your detector script (same as the CPU version)
COPY src/ /app/src/

# Create data dirs
RUN mkdir -p /data/in /data/out

ENV VERBOSE=false

# Default command
CMD ["python", "/app/src/detector.py"]
