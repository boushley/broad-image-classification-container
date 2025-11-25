FROM python:3.10-slim

WORKDIR /app

COPY ../../requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /data/assets
RUN mkdir -p /data/base-data

ENTRYPOINT ["python", "./organize.py"]
