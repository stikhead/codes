import requests
import dotenv
import os
dotenv.load_dotenv()
# 1. sending data (post request)
payload = {
    "model": "gpt-5",
    "prompt": "write a regex to match email address",
    "max_tokens": 100
}

headers = {
    "Authorization": f"Bearer {os.getenv('chatgpt')}",
    "Content-Type": "application/json"
}

response = requests.post("https://api.openai.com/v1/completions", json=payload, headers=headers)
print(response.json())


# 2. timeout and raise_for_status
try:
    # timeout the request if server takes more than 3 seconds to respond
    response = requests.get("https://api.github.com/zen", timeout=3)
    response.raise_for_status() # if server returns a 404 (not found) or 500 (server error)
    # this forces the script to throw a python exception rather than failing silently

    print("server is healthy")
except requests.exceptions.Timeout:
    print("critical: the server took too long to respond")
except requests.exceptions.HTTPError as err:
    print(f"critical: server returned an error: {err}")


# 3. connection pooling (session object)
# if script needs to ping an api for 100 times with request.get()... 
# it will be extremely slow bc it opens and closes a new network connecction each time.
# so instead, we use a session. it opens a singl3e secure tunnel. keeps it open and fires all 100 requests through,
# improving performance drastically

# ceeate a persistent session
client = requests.Session()

# set headers once and it applies to every future request
client.headers.update({"Authorization": f"Bearer {os.getenv("chatgpt")}"})

# these requests are now lightning fast bc the connection is already open
user_one = client.get("https://api.example.com/users/1")
user_two = client.get("https://api.example.com/users/2")
# 