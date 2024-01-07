import paho.mqtt.client as mqtt
from logger import Logger, EVENT_CONNECTED, EVENT_CONN_REQUEST


class MQTTClient(Logger):
    def __init__(self, client_id, broker_address, port=1883):
        self.client_id = client_id
        self.client = mqtt.Client(client_id)
        self.broker_address = broker_address
        self.port = port
        self.client.on_connect = self.on_connect
        super().__init__(device_id=client_id)

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        self.log_message(
            event_type=EVENT_CONNECTED,
            from_device='',
            to_device=self.client_id,
            message="",
        )

    def connect(self):
        self.client.connect(self.broker_address, self.port, 60)
        self.log_message(
            event_type=EVENT_CONN_REQUEST,
            from_device=self.client_id,
            to_device='',
            message="",
        )
        self.client.loop_start()
