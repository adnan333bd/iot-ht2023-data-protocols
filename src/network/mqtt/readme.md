# mqtt test steps

### run all containers from docker-compose file

inside src/network/mqtt folder:

    docker compose up --build

please wait until sub_20.csv has all the messages logged

### for diff bandwidth

change limit in thottle.sh

#### remove all containers
    
    docker rm -f $(docker ps -aq)

inside src/network/mqtt folder:

    docker compose up --build

## Debugging

### list all containers

    docker compose ps -a


### service start stop

    docker compose stop mqtt-sub

    delete all csv files inside mqtt/log/csv

    docker compose start mqtt-sub

    docker compose start mqtt-pub

## bandwidth change test with iperf3

## mqtt-pub
    
    docker compose exec -it --privileged mqtt-pub /bin/bash

    /bin/bash throttle.sh

    iperf3 -c 172.100.10.10 -p 8080 -t 30

### broker

    docker compose exec -it --privileged mqtt-broker /bin/sh

    iperf3 -s -p 8080

## pyenv setup in ubuntu

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


