# Dockerfile for server2
FROM python:3.9-slim
WORKDIR /app
COPY server2.py /app/server2.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "server2.py"]

