# Dockerfile for server1
FROM python:3.9-slim
WORKDIR /app
COPY server1.py /app/server1.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "server1.py"]

