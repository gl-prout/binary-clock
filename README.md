# Binary Clock Application

This is a simple binary clock application built with Python and Tkinter. The application displays the current time in binary format and includes a dark mode toggle.

## Prerequisites

- Docker installed on your system.
- An X11 server running on your host machine for GUI forwarding:
    - **Linux**: Ensure X11 is installed and running.
    - **Windows**: Use an X server like VcXsrv.
    - **macOS**: Use an X server like XQuartz.

## Features
- Displays the current time in binary format.
- Dark mode toggle for better visibility in low-light conditions.

## Running the Application Locally
If you prefer to run the application locally without Docker, follow these steps:
- Ensure you have Python 3 and Tkinter installed on your system:
  - For Ubuntu/Debian:
    ```bash
    sudo apt-get install python3 python3-tk
    ```
  - For Windows:
    - Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).
    - Tkinter is included with the standard Python installation.
  - For macOS:
    - Tkinter is included with the standard Python installation. If you have Homebrew, you can install Python with:
    ```bash
    brew install python
    ```
- Clone the repository:
  ```bash
  git clone https://github.com/gl-prout/binary-clock.git
  cd binary-clock
  ```
- Run the application:
  ```bash
  python3 main.py
  ```

## How to Run the Application with Docker

1. **Clone the Repository**  
   Clone the repository containing the application code:
   ```bash
   git clone https://github.com/gl-prout/binary-clock.git
   cd binary-clock
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