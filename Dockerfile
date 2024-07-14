# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install build dependencies
RUN apt-get update \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false 

# Copy only the dependency files to optimize caching
COPY pyproject.toml poetry.lock /app/

# Install project dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . /app

# Install the current directory in editable mode
RUN pip install --editable .

# Expose ports for API and UIe
EXPOSE 7651 7652

# Run the API service
CMD ["agent-shield", "run", "api"] 
# Run the UI service
# CMD ["agent-shield", "run", "ui"] 