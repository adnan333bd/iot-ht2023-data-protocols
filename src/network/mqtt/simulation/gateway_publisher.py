import time
from logger import EVENT_MSG_SENT
from mqtt_client_adapter import MQTTClient


class PublisherGateway(MQTTClient):
    def __init__(self, client_id, broker_address):        
        super().__init__(client_id=client_id, broker_address=broker_address)

    def publish_message(self, message):
        self.client.publish(self.topic, message)
        print(f"Published message: {message}")
        self.log_message(
            event_type=EVENT_MSG_SENT,
            from_device=self.client_id,
            to_device="",
            message=message,
        )


gateway = PublisherGateway(client_id="pub_1", broker_address="172.100.10.10")
gateway.connect()

time.sleep(2)

for i in range(100):
    # Publish a message
    gateway.publish_message(f"msg_{i}")
    time.sleep(1)
