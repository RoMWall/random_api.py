import requests
import os

url = "https://api.random.org/json-rpc/4/invoke"
api_key = os.environ["RANDOM_API_KEY"]

payload = {
     "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": api_key,
        "n": 10,
        "min": 0,
        "max": 100,
        "replacement": True
    },
    "id": 42
}

#payload above requests 10 random numbers between 0 and 100
r = requests.post(url, json=payload)

r.raise_for_status()

data = r.json()

print(data["result"]["random"]["data"])
