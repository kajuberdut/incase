# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container to /app
WORKDIR /app

# Install FastAPI + incase
RUN pip install fastapi[all] "incase>=0.0.12"

# Copy example.py
COPY example.py /app/example.py

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run uvicorn when the container launches
CMD ["uvicorn", "example:app", "--host", "0.0.0.0", "--port", "8000"]
