https://dev.to/abbazs/a-step-by-step-guide-for-starting-a-mosquitto-broker-service-in-a-containers-with-docker-compose-1j8i

New-Item -ItemType File -Path "log/mosquitto.log"

docker-compose up --build


docker-compose exec -it --privileged mqtt-sub /bin/bash

# Create the root class with the total bandwidth rate using htb
tc qdisc add dev eth0 root handle 1: htb default 10
tc class add dev eth0 parent 1: classid 1:1 htb rate 1mbit burst 32kbit

# Create a child class for normal traffic
tc class add dev eth0 parent 1:1 classid 1:10 htb rate 1mbit burst 32kbit

# Create a child class for traffic from a specific IP (e.g., 172.100.10.10) with lower bandwidth
tc class add dev eth0 parent 1:1 classid 1:20 htb rate 500kbit burst 32kbit

# Assign a filter to direct traffic from the specified IP to the class with lower bandwidth
source_ip="172.100.10.10"
tc filter add dev eth0 parent 1: protocol ip prio 1 u32 match ip src $source_ip flowid 1:20

