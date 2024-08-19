# client.py
import requests
import time

server1_url = 'http://server1-service'
server2_url = 'http://server2-service'

while True:
    try:
        response = requests.get(server1_url)
        print('Server 1 Response:', response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server1: {e}")
    time.sleep(1)

    try:
        response = requests.get(server2_url)
        print('Server 2 Response:', response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server2: {e}")
    time.sleep(1)
