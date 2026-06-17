import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv(
    "CRICKET_API_TOKEN"
)

url = (
    "https://api.sportmonks.com/v3/cricket/livescores"
)

params = {

    "api_token": TOKEN

}

response = requests.get(
    url,
    params=params
)

data = response.json()

print(data)