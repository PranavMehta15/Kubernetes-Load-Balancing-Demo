# server1.py
from flask import Flask, request
import time
import logging

app = Flask(__name__)

logging.basicConfig(filename='/app/server1.log', level=logging.INFO)

@app.route('/')
def hello():
    time.sleep(1)  # Simulate delay
    message = 'Hello from Server 1!'
    logging.info(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {message}')
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

