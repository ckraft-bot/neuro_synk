import requests

url = "http://127.0.0.1:5000/api/generate"
data = {"prompt": "Tell me a joke."}

response = requests.post(url, json=data)

print(response.json())  # Print the LLM's response
