import requests

# Getting the response from the ISS data
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# automatically raise an exception for corresponing error.
response.raise_for_status()

# TODO: Get longitude and latitude of the ISS
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)