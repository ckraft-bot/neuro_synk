# Use Ollama as the base image
FROM ollama/ollama:latest

# Expose Ollama's default port
EXPOSE 11434

# Copy the entry script and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the script as the entrypoint
CMD ["/entrypoint.sh"]