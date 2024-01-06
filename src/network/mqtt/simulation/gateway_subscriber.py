import time
from logger import EVENT_MSG_RECVD
from mqtt_client_adapter import MQTTClient


class SubscriberGateway(MQTTClient):
    def __init__(self, client_id, broker_address):        
        super().__init__(client_id=client_id, broker_address=broker_address)
        self.client.on_message = self.on_message

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode()
        print(f"Received message : {payload} on topic: {topic}")
        self.log_message(
            event_type=EVENT_MSG_RECVD,
            from_device="",
            to_device=self.client_id,
            message=payload,
        )

    def subscribe(self):
        self.client.subscribe(self.topic)


if __name__ == '__main__':
    gateway = SubscriberGateway(client_id="sub_1", broker_address="172.100.10.10")
    gateway.connect()
    gateway.subscribe()
    time.sleep(5000)
