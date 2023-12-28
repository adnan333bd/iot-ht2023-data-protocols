# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY helloworld.py /app/

# Run helloworld.py when the container launches
CMD ["python", "./helloworld.py"]