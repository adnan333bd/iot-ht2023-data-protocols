from gateway_publisher import PublisherGateway


def test():
    gateway = PublisherGateway(client_id="pub_1", broker_address="172.100.10.10")
    gateway.connect()
    for i in range(20):
        # Publish a message
        gateway.publish_message(f"msg_{i}")


if __name__ == "__main__":
    test()
