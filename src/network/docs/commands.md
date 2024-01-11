# pub 1

docker-compose exec -it --privileged mqtt-pub /bin/bash

./throttle.sh

iperf3 -c 172.100.10.10 -p 8080 -t 30

# broker

docker-compose exec -it --privileged mqtt-broker /bin/sh

iperf3 -s -p 8080

# set 100mbit