https://dev.to/abbazs/a-step-by-step-guide-for-starting-a-mosquitto-broker-service-in-a-containers-with-docker-compose-1j8i

New-Item -ItemType File -Path "log/mosquitto.log"

docker-compose up --build


docker-compose exec -it mqtt-sub /bin/bash


# Create the root class with the total bandwidth rate
tc qdisc add dev eth0 root handle 1: htb default 10
tc class add dev eth0 parent 1: classid 1:1 htb rate 1mbit burst 32kbit latency 400ms

# try this -

# Create the root class with the total bandwidth rate using htb
tc qdisc add dev eth0 root handle 1: htb default 10
tc class add dev eth0 parent 1: classid 1:1 htb rate 1mbit burst 32kbit

# Create a child class for normal traffic
tc class add dev eth0 parent 1:1 classid 1:10 htb rate 1mbit burst 32kbit

# Create a child class for traffic with latency using netem
tc qdisc add dev eth0 parent 1:10 handle 10: netem delay 400ms

# Now you can assign filters to direct specific traffic to the appropriate class

