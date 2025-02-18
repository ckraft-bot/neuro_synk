#!/bin/bash

# Start Ollama in the background
ollama serve &

# Give Ollama some time to initialize
sleep 10

# Pull the Gemma 2B model
ollama pull gemma2:2b

# Run the status checks
ollama ps
ollama list

# Keep the container running
wait $!
