# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the script for controlling network speed and the requirements file
COPY simulation/gateway_publisher.py /app/
COPY simulation/requirements.txt /app/
COPY Dockerfile.network /app/

# Install additional dependencies for network emulation
RUN apt-get update && \
    apt-get install -y iproute2

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set up low bandwidth using tc when the container launches
CMD ["bash", "Dockerfile.network"]
