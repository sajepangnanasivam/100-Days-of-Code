import requests
import pandas as pd
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "kljsvnaa209471nv8sjn2"
USERNAME = "sajepangnanasivam"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# TODO 1: Create a user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.json())

# TODO 2: Create a Graph in Pixela (POST - /v1/users/<username>/graphs)
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Water Graph",
    "unit": "ml",
    "type": "float",
    "color": "ajisai"
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)

# TODO 3: Post a pixel
SUBMIT_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
# today = datetime(year=2022, month=3, day=12)
today = datetime.now()

PIXELA_DATA = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many ml of waters did you drink?\t"),
}

response = requests.post(url=SUBMIT_PIXEL_ENDPOINT, json=PIXELA_DATA, headers=headers)
print(response.text)

# TODO 4: Update pixel
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

UPDATE_DATA = {
    "quantity": "20.5"
}

response = requests.put(url=UPDATE_ENDPOINT, json=UPDATE_DATA, headers=headers)
print(response.text)

# TODO 4: Delete Pixel
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(response.text)