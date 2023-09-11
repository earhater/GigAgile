# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Poetr
# Install system dependencies

# Install Poetry
RUN pip3 install poetry

# Set the working directory to /app
WORKDIR /app

# Copy only the dependency files and install them separately to utilize Docker layer caching
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-dev

# Copy the rest of the application code into the container
COPY . /app/

# Expose any necessary ports
# EXPOSE 8000

# Define the command to run your application (replace with your actual entry point)
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
