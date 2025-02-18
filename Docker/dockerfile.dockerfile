# Use Ollama as the base image
FROM ollama/ollama:latest

# Pull the Gemma 2B model inside the container
RUN ollama pull gemma2:2b

# Copy the entry script and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose Ollama's default port
EXPOSE 11434

# Use the script as the entrypoint
CMD ["/entrypoint.sh"]
