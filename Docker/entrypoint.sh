#!/bin/bash
ollama serve &   # Start Ollama in the background
sleep 5          # Wait for initialization
ollama ps
ollama list
wait             # Keep the container running
