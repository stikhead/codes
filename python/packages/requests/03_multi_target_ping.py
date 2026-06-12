import requests

client = requests.Session()

users = ["stickhead", "tourist", "Benq"]

for user in users:
    
    try:
        response = client.get(f"https://codeforces.com/api/user.info?handles={user}")

        response.raise_for_status()

        if(200<= response.status_code < 300):
            print(response.json())

    except requests.exceptions.HTTPError as e:
      print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")