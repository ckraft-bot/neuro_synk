import requests

# OLLAMA_URL = "http://157.230.187.207:11434"

# try:
#     response = requests.get(OLLAMA_URL)
#     print(response.status_code)
#     print(response.text)
# except Exception as e:
#     print(f"Error: {e}")


OLLAMA_URL = "http://157.230.187.207:11434/api/generate"

def get_ollama_response(data):
    try:
        response = requests.post(OLLAMA_URL, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return response.json()  # Assuming Ollama returns JSON
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ollama: {e}")
        return None

# Example data (replace with actual required data)
data = {
    "text": "Hello, Ollama!",
    "context": "Sample context"
}

response = get_ollama_response(data)
if response:
    print("Ollama response:", response)
else:
    print("Failed to get a response.")
