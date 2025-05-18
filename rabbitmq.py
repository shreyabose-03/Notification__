import pika
import json
import time

MAX_RETRIES = 3

def publish_to_queue(data: dict):
    retry_count = 0
    while retry_count < MAX_RETRIES:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
            channel = connection.channel()
            channel.queue_declare(queue="notifications")
            channel.basic_publish(
                exchange="",
                routing_key="notifications",
                body=json.dumps(data)
            )
            connection.close()
            break
        except Exception as e:
            retry_count += 1
            print(f"Retry {retry_count}/{MAX_RETRIES} - Could not publish: {e}")
            time.sleep(2)
