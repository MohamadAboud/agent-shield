# Use Python 11.0 as the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy only the dependency files to optimize caching
COPY poetry.lock pyproject.toml /app/

# Install project dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . /app/

RUN pip install --editable .

# Expose the ports for both the API and UI
EXPOSE 7651
EXPOSE 7652

# Run the application
CMD ["agent-shield", "run", "api"]
