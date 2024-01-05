# iot-ht2023-data-protocols

Group 2-1
Golam Sobhani Chowdhury
Adit Ishraq
Jaber Ahmed

4, 5 MQTT
- python code docker e test: sh command to container in python
- simulation lots of object
- change container for network contidition
- test again


- log write working in python, preferebly csv
- sanitize logs
- test run
- read log and calc statistics

6, 7 XMPP
- 
8 report


=========================================================

pub_sub_id  event_type            timestamp
-------------------------------------------
pub_1       connect_requested     123654
pub_1       connect_completed     126485

event_types: connect_requested, connect_completed, message_sent, message_received

==========================================================


mqtt-pub:
    image: eclipse-mosquitto:latest
    command: sh -c "mosquitto_pub -h mqtt-broker -t test -m 'Hello World' -u admin -P password"
    depends_on:
      - mqtt-broker
    networks:
      mqtt-net:
        ipv4_address: 172.100.10.11

mqtt-sub:
    build: sub_container/
    depends_on:
      - mqtt-broker
    networks:
      mqtt-net:
        ipv4_address: 172.100.10.14

mqtt-sub-cli:
    image: eclipse-mosquitto:latest
    command: sh -c "mosquitto_sub -h mqtt-broker -t "/device" -u admin -P password"
    depends_on:
      - mqtt-broker
    networks:
      mqtt-net:
        ipv4_address: 172.100.10.12