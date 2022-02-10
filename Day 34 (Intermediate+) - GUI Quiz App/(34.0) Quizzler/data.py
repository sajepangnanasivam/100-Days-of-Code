import requests
API_URL = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"

response = requests.get(url=API_URL)
response.raise_for_status()
question_data = response.json()["results"]