import time
from logger import EVENT_MSG_RECVD, Logger
from mqtt_client_adapter import MQTTClient
from constants import BROKER_ADDRESS, NUMBER_OF_PUB_SUB_GATEWAYS


class SubscriberGateway2(MQTTClient):
    def __init__(self, client_id, broker_address):
        super().__init__(client_id=client_id, broker_address=broker_address)
        self.topic = f"/pub_{client_id[4:]}"
        self.client.on_message = self.on_message

    def on_message(self, client, userdata, msg):
        # topic = msg.topic
        payload = msg.payload.decode()
        # print(f"Received message : {payload} on topic: {topic}")
        self.log_message(
            event_type=EVENT_MSG_RECVD,
            from_device="",
            to_device=self.client_id,
            message=payload,
        )

    def subscribe(self):
        self.client.subscribe(self.topic)


if __name__ == "__main__":
    gateways = []
    for i in range(NUMBER_OF_PUB_SUB_GATEWAYS):
        gateway = SubscriberGateway2(
            client_id=f"su2_{i+1}", broker_address=BROKER_ADDRESS
        )
        gateway.connect()
        gateways.append(gateway)

    for gateway in gateways:
        gateway.subscribe()

    while True:
        time.sleep(5)
        Logger.dump_logs()
