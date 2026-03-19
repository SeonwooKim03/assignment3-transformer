import requests

response = requests.post(
    "http://127.0.0.1:5000/transform",
    json={"voltage": 2.5}
)

print(response.status_code)
print(response.json())