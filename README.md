# iot-ht2023-data-protocols
From_Device_ID,To_Device_ID,Event_Type,Message,Time_Stamp
sub_1,,EVENT_CONNECTED,,2024-01-06 22:09:21.079607
,sub_1,EVENT_MSG_RECD,msg_0,2024-01-06 22:09:43.998265
,sub_1,EVENT_MSG_RECD,msg_1,2024-01-06 22:09:44.048644
,sub_1,EVENT_MSG_RECD,msg_2,2024-01-06 22:09:44.099294

From_Device_ID,To_Device_ID,Event_Type,Message,Time_Stamp
pub_1,,EVENT_CONNECTED,,2024-01-06 22:09:43.797621
pub_1,,EVENT_MSG_SENT,msg_0,2024-01-06 22:09:43.996928
pub_1,,EVENT_MSG_SENT,msg_1,2024-01-06 22:09:44.047709
pub_1,,EVENT_MSG_SENT,msg_2,2024-01-06 22:09:44.098313

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


      - target: 9001
        published: 9001
        protocol: tcp
        mode: host

