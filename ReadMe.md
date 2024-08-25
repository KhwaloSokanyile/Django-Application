# Django Task Management Application

This is a simple Django-based task management application where users can create, complete, delete, and edit their tasks. The application supports user authentication.

## Features
- User authentication (Sign up, Log in, Log out)
- Create new tasks
- Mark tasks as completed
- Delete tasks
- Edit existing tasks
- View completed tasks with completion date and time

## Prerequisites

### Local Setup

1. **Python 3.10 or later**: Ensure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **pip**: Python's package installer. It is included with Python.

3. **Virtual Environment (optional but recommended)**: Helps to manage dependencies.

### Docker Setup

1. **Docker**: Ensure Docker is installed. You can download it from [docker.com](https://www.docker.com/get-started).

## Running Locally

1. **Clone the Repository**

    ```bash
    git clone https://your-repository-url.git
    cd your-repository-directory
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

    The application should now be running at `http://127.0.0.1:8000/`.

## Running with Docker

1. **Build the Docker Image**

    Make sure you are in the directory containing the Dockerfile (`.\Django-Application`):

    ```bash
    docker build -t django-application .
    ```

2. **Run the Docker Container**

    ```bash
    docker run -p 8000:8000 django-application
    ```

    The application should now be accessible at `http://localhost:8000/`.

3. **Running Docker Commands in Windows**

    If you encounter issues on Windows, ensure you have Docker Desktop running and your Docker daemon is configured correctly.

## Troubleshooting

- **Missing `manage.py` File**: Ensure the `manage.py` file is correctly placed in the `task_manager` directory, and that it is copied to the Docker container correctly.

- **Database Errors**: Make sure you have run `migrate` to set up the database schema. Check the `DATABASES` setting in `settings.py` if using Docker.

- **Port Conflicts**: Ensure no other applications are using port 8000 on your host machine.

- **Local Logs**: Check the terminal output for errors when running the server locally.

- **Docker Logs**: Use `docker logs <container_id>` to view logs for the running Docker container.

