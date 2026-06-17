# check_plan.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("CRICKET_API_TOKEN")

url = "https://api.sportmonks.com/v3/cricket/fixtures"

response = requests.get(
    url,
    params={
        "api_token": TOKEN
    }
)

print(response.status_code)
print(response.text)