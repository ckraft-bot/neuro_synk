import ollama
# to find the ollama modelsavailable ```ollama list```
# if need to pull the model then use this command ```ollama pull gemma2:2b```

response = ollama.chat(model='gemma:2b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
