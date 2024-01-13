from logger import EVENT_MSG_SENT
from mqtt_client_adapter import MQTTClient


class PublisherGateway(MQTTClient):
    def __init__(self, client_id, broker_address):
        super().__init__(client_id=client_id, broker_address=broker_address)        
        self.topic = f"/{client_id}"
        self.client.on_publish = self.on_publish
        self.message = ''

    def publish_message(self, message):
        self.client.publish(self.topic, message)
        self.message = message
        # print(f"Published message: {message}")

    def on_publish(self, client, userdata, mid):
        # print(f"Published message: {self.message}")
        self.log_message(
            event_type=EVENT_MSG_SENT,
            from_device=self.client_id,
            to_device="",
            message=self.message,
        )
       

