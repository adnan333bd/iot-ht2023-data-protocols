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
