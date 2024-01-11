# Environment requirements

- Docker desktop installed in MacOS or Ubuntu (other linux based OS)

# How to run the docker compose file

Inside /mqtt folder


    docker-compose up  --build

files will be generated inside /mqtt/log/csv after a minutes or so.

# Design of the Simulation 



In the simulation scenarios, there are two type of objects - publisher gateway and subscriber gateway. A ‘subscriber gateway’ represents a raspberry PI that only subscribe to messages and ‘publisher gateway’ is another raspberry pi that only publishes messages to a topic.( For simplicity, we defined these two types of gateways)


A publisher gateway with client id pub_1 would be sending message to a topic - ‘pub_1’ (topic name = publisher’s client id) and subscriber gateway with client id sub_1 would subscribe to a corresponding topic ‘pub_1’. This is a one to one message transfer, and suffix of the client id (1,2,3 … ) makes a pairing of the gateways for communication. In implementation, each gateway should be a python object with capability of connecting as a client to an MQTT broker.


One running container called ‘pub container’ with ip address 172.100.10.13 would be acting as a host machine for all publisher gateways. Number of gateways in a test run should be configurable with a single constant in python code. Similarly one container with ip address 172.100.10.14 would host all subscriber gateways (python objects). All gateways will connect to the broker, running in a container with ip address 172.100.10.10. All three containers are in the same network 172.100.10.0/24.

In a single test run, all messages will be uniquely identifiable, like msg_1, msg_2. This identity will be used to calculate the delivery latency of a message. Each pubisher gateway would be sending n number of messages to a paired subscriber gateway, in a single test run. Value of n should be configurable by single constant in python.



 mysql-client:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: 'db'
      # So you don't have to use root, but you can if you like
      MYSQL_USER: 'user'
      # You can use whatever password you like
      MYSQL_PASSWORD: '123'
      # Password for root access
      MYSQL_ROOT_PASSWORD: '123'
    ports:
      # <Port exposed> : <MySQL Port running inside container>
      - '3309:3306'
    expose:
      # Opens port 3306 on the container
      - '3306'
      # Where our data will be persisted
    volumes:
      - type: bind
        source: ./srv/db
        target: /var/lib/mysql
        read_only: false
    networks:
      xmpp-net:
        ipv4_address: 172.100.20.20


ws://host.docker.internal:7070/ws/