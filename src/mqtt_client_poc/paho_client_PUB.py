import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("/adnan")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("py_pub_1")
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

#for i in range(1, 20):
#    client.publish("/winter", "Hello aatif" + str(i))

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()

# Start the loop to handle network communication and callbacks
client.loop_start()

# Continuous loop for taking user input and publishing it
while True:
    user_input = input("Enter your message: ")
    
    # Publish the user input to the specified topic
    client.publish("/winter", user_input)