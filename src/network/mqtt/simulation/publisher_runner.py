from gateway_publisher import PublisherGateway
import time
from logger import Logger

from constants import (
    BROKER_ADDRESS,
    NUMBER_OF_PUB_SUB_GATEWAYS,
    NUMBER_OF_MSG_PER_GATEWAY,
)


def counter_generator():
    count = 0
    while True:
        yield count
        count += 1


count_gen = None


def send_message(gateway):
    for i in range(NUMBER_OF_MSG_PER_GATEWAY):
        message_id = next(count_gen)
        gateway.publish_message(f"msg_{message_id}")
        time.sleep(0.05)


def test():
    gateways = []
    for i in range(NUMBER_OF_PUB_SUB_GATEWAYS):
        gateway = PublisherGateway(
            client_id=f"pub_{i+1}", broker_address=BROKER_ADDRESS
        )
        gateway.connect()
        gateways.append(gateway)
    time.sleep(5)
    for gateway in gateways:
        send_message(gateway)


if __name__ == "__main__":
    count_gen = counter_generator()
    time.sleep(30)
    test()
    time.sleep(5)
    Logger.dump_logs()
