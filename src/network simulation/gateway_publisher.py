import paho.mqtt.client as mqtt
import time
import csv
import os


# path
path = '/mosquitto/log/csv/csv'

# Ensure the directory exists, create it if not
if not os.path.exists(path):
    os.makedirs(path)

current_time = time.strftime("%Y-%m-%d %H:%M:%S")
# Specify the file name
filename = 'publisher.csv'

# Construct the full file path
filepath = os.path.join(path, filename)

fieldnames = ["Topic", "Event Type", "Message", "Time"]
topic_to_publish = "/device"
message_to_publish = "device_id:1;state:on"

class PublisherGateway:
    def __init__(self, client_id, broker_address, port=1883):
        self.client = mqtt.Client(client_id)
        self.broker_address = broker_address
        self.port = port
        self.topic = None
        self.message = None

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        data = {"Topic": topic_to_publish, "Event Type": "connection-completed", "Message": message_to_publish, "Time": current_time}

        try:
            with open(filepath, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Write header if the file is empty
                if file.tell() == 0:
                    writer.writeheader()

                # Write new data
                writer.writerow(data)
            print(f'CSV file created successfully at: {filepath}')
        except Exception as e:
            print(f'Error creating CSV file: {e}')

    def on_message(self, client, userdata, msg):
        # print(f"({self.client.client_id}) Received message : {msg.payload.decode()}")
        pass

    def on_publish(mqttc, obj, mid):
        print("mid: " + str(mid))

    def connect(self):
        self.client.connect(self.broker_address, self.port, 60)
        data = {"Topic": topic_to_publish, "Event Type": "connection-requested", "Message": message_to_publish, "Time": current_time}

        try:
            with open(filepath, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Write header if the file is empty
                if file.tell() == 0:
                    writer.writeheader()

                # Write new data
                writer.writerow(data)
            print(f'CSV file created successfully at: {filepath}')
        except Exception as e:
            print(f'Error creating CSV file: {e}')

        self.client.loop_start()

    def publish_message(self, topic, message):
        self.topic = topic
        self.message = message
        self.client.publish(self.topic, self.message)
        # print(f"Published message: {self.message}")

        data = {"Topic": self.topic, "Event Type": "message-sent", "Message": self.message, "Time": current_time}

        try:
            with open(filepath, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Write header if the file is empty
                if file.tell() == 0:
                    writer.writeheader()

                # Write new data
                writer.writerow(data)
            print(f'CSV file created successfully at: {filepath}')
        except Exception as e:
            print(f'Error creating CSV file: {e}')


gateway = PublisherGateway(client_id="ras_pi_pub_1", broker_address="172.100.10.10")
gateway.connect()

time.sleep(2)

# Publish a message
gateway.publish_message(topic_to_publish, message_to_publish)
time.sleep(1)
