import requests

response1 = requests.delete("http://localhost:8080/items/1")

response = requests.get("http://localhost:8080/items")

actual = len(response.json())
expected = 2
print(response.text)
assert expected == actual