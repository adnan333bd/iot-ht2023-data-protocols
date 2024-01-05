import paho.mqtt.client as mqtt
import time


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

    def on_message(self, client, userdata, msg):
        # print(f"({self.client.client_id}) Received message : {msg.payload.decode()}")
        pass

    def connect(self):
        self.client.connect(self.broker_address, self.port, 60)
        self.client.loop_start()
        time.sleep(2)

    def publish_message(self, topic, message):
        self.topic = topic
        self.message = message
        self.client.publish(self.topic, self.message)
        # print(f"Published message: {self.message}")


gateway = PublisherGateway(client_id="ras_pi_pub_1", broker_address="172.100.10.10")
gateway.connect()

# Publish a message
topic_to_publish = "/device"
message_to_publish = "device_id:1;state:on"
gateway.publish_message(topic_to_publish, message_to_publish)
time.sleep(10)