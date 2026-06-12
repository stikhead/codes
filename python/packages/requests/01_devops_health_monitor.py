import os
import requests
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("PROD_API_KEY")

response = requests.get("https://api.github.com/zen")

print(key)
print(response.text)
print(response.json)