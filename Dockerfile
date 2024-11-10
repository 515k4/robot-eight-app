# Use the official Python image as a base
FROM python:3.12-slim

# Run as non root
RUN mkdir -m 755 /app
RUN useradd appuser -u 10001 --user-group --home-dir /app
RUN chown appuser:appuser /app -R
USER 10001

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY --chown=appuser requirements.txt .

# Install dependencies
RUN python3 -mvenv /app/venv && \
    . /app/venv/bin/activate && \
    /app/venv/bin/pip install -r requirements.txt

# Copy the FastAPI application code into the container
COPY --chown=appuser . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the application with uvicorn
CMD ["/app/venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
