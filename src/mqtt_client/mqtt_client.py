import paho.mqtt.client as mqtt
import time

# MQTT broker details
broker_address = "127.0.0.1"
port = 1883
topic = "/connect/paho_mqtt_client"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic when connected
    client.subscribe(topic)

# Callback when a message is received from the broker
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# Create an MQTT client
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port, 60)

# Start the background thread for handling MQTT communication
client.loop_start()

# Allow some time for the subscription
time.sleep(2)

# Publish a message
message_to_publish = "Trying to publish and subscribe the messages from paho-mqtt!"
client.publish(topic, message_to_publish)
print(f"Published message: {message_to_publish}")

# Keep the script running for a while to allow on_message to be called
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()