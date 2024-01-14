## install nodejs in ubuntu

#### from https://github.com/nodesource/distributions#installation-instructions
curl -fsSL https://deb.nodesource.com/setup_21.x | sudo -E bash - &&\
sudo apt-get install -y nodejs

## run docker compose up to deploy the containers
docker compose up --build

- after first run the sender and receiver wont connect to 172.100.39.10 (server)
- go to admin console at localhost:9090 and setup openfire with embeded db, domain host.docker.internal
- create two users with password 123 - goch6657@example.com , iamadit@example.com

## run the reciever container in a differenent terminal

see what are the containers running

    docker compose ps -a

start the receiver service

    docker compose start xmpp-receiver

see the logs

    docker compose logs xmpp-receiver

## run the sender container in a differenent terminal

    docker compose start xmpp-sender

    docker compose logs xmpp-sender

(to run again later, you can use docker compose restart xmpp-sender)



## debugging

shell in the container:
docker compose exec -it --privileged xmpp-receiver /bin/bash

# docker compose commands




# run all containers from compose file config
docker compose up --build


## 



# remove all containers
docker rm -f $(docker ps -aq)

# run pub again, to test again
docker compose ps -a
docker compose start mqtt-mqtt-pub-1

# stop all running containers
docker stop $(docker ps -a)

# bandwidth change 
## mqtt-pub 
docker compose exec -it --privileged mqtt-pub /bin/bash

/bin/bash throttle.sh

iperf3 -c 172.100.10.10 -p 8080 -t 30

# broker

docker compose exec -it --privileged mqtt-broker /bin/sh

iperf3 -s -p 8080

# set 100mbit
change limit in thottle.sh

# pyenv setup in ubuntu

apt update; apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash

### Load pyenv automatically by appending
### the following to
### ~/.bash_profile if it exists, otherwise ~/.profile (for login shells)
### and ~/.bashrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

### Restart your shell for the changes to take effect.

### Load pyenv-virtualenv automatically by adding
### the following to ~/.bashrc:

eval "$(pyenv virtualenv-init -)"

source ~/.bashrc && exec $SHELL


### openfire 

docker rm -f $(docker ps -aq)


