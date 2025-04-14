# Binary Clock Application

This is a simple binary clock application built with Python and Tkinter. The application displays the current time in binary format and includes a dark mode toggle.

## Prerequisites

- Docker installed on your system.
- An X11 server running on your host machine for GUI forwarding:
    - **Linux**: Ensure X11 is installed and running.
    - **Windows**: Use an X server like VcXsrv.
    - **macOS**: Use an X server like XQuartz.

## How to Run the Application with Docker

1. **Clone the Repository**  
   Clone the repository containing the application code:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Build the Docker Image**  
   Build the Docker image using the provided `Dockerfile`:
   ```bash
   docker build -t binary-clock .
   ```

3. **Run the Docker Container**  
   Run the container with the necessary environment variables and volume bindings for GUI forwarding:
   ```bash
   docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix binary-clock
   ```

    - **Linux**: The above command should work as is.
    - **Windows**: Ensure VcXsrv is running and allow access to the X server.
    - **macOS**: Start XQuartz and enable "Allow connections from network clients."

4. **View the Application**  
   The binary clock application should now appear on your screen.

## Notes

- If you encounter issues with GUI forwarding, ensure your X server is properly configured and running.
- For Windows and macOS, you may need to set the `DISPLAY` environment variable manually. For example:
  ```bash
  export DISPLAY=host.docker.internal:0
  ```