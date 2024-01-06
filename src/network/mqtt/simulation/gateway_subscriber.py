import paho.mqtt.client as mqtt
import time
import csv
import os

fieldnames = ["Topic", "Event Type", "Message", "Time"]

class SubscriberGateway:
    def __init__(self, client_id, broker_address, port=1883):
        self.client = mqtt.Client(client_id)
        self.broker_address = broker_address
        self.port = port
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        # connect end
        print(f"Connected with result code {rc}")

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Received message : {payload} on topic: {topic} at time {current_time}")
        #Define the path where you want to create the CSV file
        path = '/mosquitto/log/csv/csv'

        # Ensure the directory exists, create it if not
        if not os.path.exists(path):
            os.makedirs(path)

        data = {"Topic": topic, "Event Type": "message-received", "Message": payload, "Time": current_time}

        # Specify the file name
        filename = 'subscriber.csv'

        # Construct the full file path
        filepath = os.path.join(path, filename)

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

    def connect(self):
        # connect start
        self.client.connect(self.broker_address, self.port, 60)
        self.client.loop_start()

    def subscribe(self):
        self.client.subscribe("/device")


gateway = SubscriberGateway(client_id="ras_pi_sub_1", broker_address="172.100.10.10")
gateway.connect()
gateway.subscribe()
# gateway.be_alive()
time.sleep(50)
