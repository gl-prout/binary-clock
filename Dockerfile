# Use an official Python base image
FROM python:3.10-slim

# Install dependencies for GUI applications
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY main.py /app/

# Set the display environment variable for GUI forwarding
ENV DISPLAY=:0

# Expose the port for X11 forwarding (optional, depends on your setup)
EXPOSE 6000

# Run the application
CMD ["python", "main.py"]
