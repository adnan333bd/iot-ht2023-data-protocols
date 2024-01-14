

## 1 Run docker compose up to deploy the containers

    docker compose up --build

- after first run the sender and receiver wont connect to 172.100.39.10 (server is not ready yet)
- go to admin console at localhost:9090 (in host machine)  and setup openfire with embeded db, domain host.docker.internal
- create two users with password 123 - goch6657@example.com , iamadit@example.com

you should be able to see in your terminal (first time only, when configured)

openfire         | Missing database schema for openfire. Attempting to install...
openfire         | Database update successful.
openfire         | Admin console listening at http://host.docker.internal:9090
openfire         | Successfully loaded plugin 'search'.
openfire         | Finished processing all plugins.

### 2 Run the sender container in a seperate terminal

Delete the csv files generated.

    docker compose start xmpp-sender

    docker compose logs xmpp-sender

(to run again later, you can use docker compose restart xmpp-sender)

wait until, pub_1.csv and sub_1.csv have 1000 messages each.


## 3 Bandwidth control & test for a diff. bandwidth

## 5 set 100mbit/sec for icmp

Change limit in /xmpp/sender/thottle.sh

    LIMIT=100mbit

Then deploy the containers again (from step 1 above)


### Testing bandwidth change for icmp

#### In sender container

    docker compose exec -it --privileged xmpp-sender /bin/bash

    hping3 --icmp -c 50 -i 1 172.100.39.10

    tcptrack -i eth0



## Debugging if required

### Remove all containers

    docker rm -f $(docker ps -aq)

### shell in the container:

    docker compose exec -it --privileged xmpp-sender /bin/bash
    docker compose exec -it --privileged xmpp-receiver /bin/bash

## Dev environment

## Install nodejs in ubuntu

#### from https://github.com/nodesource/distributions#installation-instructions
curl -fsSL https://deb.nodesource.com/setup_21.x | sudo -E bash - &&\
sudo apt-get install -y nodejs


