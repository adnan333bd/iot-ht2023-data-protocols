import paho.mqtt.client as mqtt
import time

class Gateway:
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
        print(f"Received message: {msg.payload.decode()}")

    def connect(self):
        self.client.connect(self.broker_address, self.port, 60)
        self.client.loop_start()
        time.sleep(2)

    def publish_message(self, topic, message):
        self.topic = topic
        self.message = message
        self.client.publish(self.topic, self.message)
        print(f"Published message: {self.message}")

    def run_forever(self):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.client.loop_stop()
            self.client.disconnect()


gateway = Gateway(client_id="py_pub_1", broker_address="127.0.0.1")


gateway.connect()

# Publish a message
topic_to_publish = "/adit"
message_to_publish = "aaaaaaaaaaaaaaa eeeeeee iiii!"
gateway.publish_message(topic_to_publish, message_to_publish)


# Keep the script running for a while to allow on_message to be called
#gateway.run_forever()