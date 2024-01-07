https://dev.to/abbazs/a-step-by-step-guide-for-starting-a-mosquitto-broker-service-in-a-containers-with-docker-compose-1j8i

New-Item -ItemType File -Path "log/mosquitto.log"

docker-compose up --build


docker-compose exec -it --privileged mqtt-sub /bin/bash



