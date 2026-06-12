import requests
import os
import dotenv
dotenv.load_dotenv()

payload = {
    "content": "🚨 **CRITICAL: API Health Monitor**",
    "embeds": [{
        "title": "Server Status",
        "description": "The Codeforces API is currently online.",
        "color": 5814783
    }]
}

url = os.getenv('discord_webhook')
try: 
    response = requests.post(url, json=payload, timeout=5)

    response.raise_for_status()
    if(200<=response.status_code <300):
        print(response.status_code)
except requests.exceptions.Timeout:
    print("request failed")
except requests.exceptions.HTTPError:
    print("server error")