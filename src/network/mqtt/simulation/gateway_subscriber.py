import paho.mqtt.client as mqtt


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
        print(f"Received message : {msg.payload.decode()}")

    def connect(self):
        # connect start
        self.client.connect(self.broker_address, self.port, 60)
        self.client.loop_start()

    def subscribe(self):
        self.client.subscribe("/device")

    def be_alive(self):
        self.client.loop_forever()


gateway = SubscriberGateway(client_id="ras_pi_sub_1", broker_address="172.100.10.10")
gateway.connect()
gateway.subscribe()
gateway.be_alive()
