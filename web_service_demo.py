import requests

BASE = "https://jsonplaceholder.typicode.com"

# 1. GET request
print("--- GET ---")
r = requests.get(f"{BASE}/posts/1")
print("Status:", r.status_code)
print("Title:", r.json()["title"])

# 2. POST request
print("\n--- POST ---")
new_post = {"title": "Learning APIs", "body": "Python is fun", "userId": 1}
r = requests.post(f"{BASE}/posts", json=new_post)
print("Status:", r.status_code)
print(r.json())

# 3. Error handling
print("\n--- ERROR HANDLING ---")
try:
    r = requests.get(f"{BASE}/posts/99999", timeout=5)
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("Server returned an error:", err)
except requests.exceptions.RequestException as err:
    print("Network problem:", err)
