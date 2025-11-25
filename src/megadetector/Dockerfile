FROM zaandahl/mewc-detect:6.0
# Workdir
WORKDIR /app

RUN mv /code/md_v1000.0.0-redwood.pt /app/md_v1000.0.0-redwood.pt
RUN rm -rf /code

# Copy your detector script
COPY ../lib /app/src/lib
COPY . /app/src/megadetector

# Create data dirs
RUN mkdir -p /data

ENV VERBOSE=false

# Default command
CMD ["python", "/app/src/megadetector/detector.py"]
