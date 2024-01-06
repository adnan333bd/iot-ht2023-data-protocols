https://dev.to/abbazs/a-step-by-step-guide-for-starting-a-mosquitto-broker-service-in-a-containers-with-docker-compose-1j8i

New-Item -ItemType File -Path "log/mosquitto.log"

docker-compose up --build


docker-compose run mqtt-mqtt-pub-1 sh -c "python app/test_runner.py"

docker-compose exec -it mqtt-sub /bin/bash

