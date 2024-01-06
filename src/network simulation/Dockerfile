# Use the official Ubuntu base image
FROM ubuntu:latest

# Install required dependencies
RUN apt-get update && \
    apt-get install -y iproute2

# Simulate low bandwidth using tc
CMD tc qdisc add dev eth0 root tbf rate 512kbit burst 32kbit latency 400ms && \
    # Add your application start command here
    # For example, if it's a web server:
    apt-get install -y apache2 && \
    service apache2 start && \
    tail -f /dev/null

# Cleanup tc rules after the container exits
CMD tc qdisc del dev eth0 root
