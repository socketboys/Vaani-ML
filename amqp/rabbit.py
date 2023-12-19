import pika
import json
from file_ops import download_file
# from scripts.pipeline_ai import multi_process


class Rabbit:
    producer_channel: pika.adapters.blocking_connection.BlockingChannel = None
    POOL_EXCHANGE = 'pool'
    POOL_ROUTING_KEY = 'poolkey'

    def callback(self, channel, method, properties, body):
        msg = json.loads(body)
        print(msg)
        print(msg["euid"])
        print(msg['link'])
        print(msg['language'])
        print(msg['email_id'])

        # download function
        download_file(msg["link"], msg["euid"] + , "/data/input")

        # multi_process(msg.input_dir, msg.audioname, msg.lang)
        # clean residual files
        # upload to spaces
        # publish function

        self.producer_channel.basic_publish(exchange=Rabbit.POOL_EXCHANGE, routing_key=Rabbit.POOL_ROUTING_KEY, body="translation done", )
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def __init__(self):
        RABBIT_URL = 'amqp://guest:guest@localhost:5672'

        TRANSLATION_ROUTING_KEY = 'translationkey'
        TRANSLATION_QUEUE_NAME = 'translation_pipeline'
        TRANSLATION_EXCHANGE = 'translation'

        POOL_QUEUE_NAME = 'update_pool'

        self.connection = pika.BlockingConnection(pika.URLParameters(RABBIT_URL))

        self.producer_channel = self.connection.channel()
        self.producer_channel.queue_declare(queue=POOL_QUEUE_NAME, auto_delete=False, durable=True, arguments={'x-queue-type': 'quorum'})

        self.consumer_channel = self.connection.channel()
        self.consumer_channel.queue_declare(queue=TRANSLATION_QUEUE_NAME, auto_delete=False, durable=True, arguments={'x-single-active-consumer': True})
        self.consumer_channel.queue_bind(queue=TRANSLATION_QUEUE_NAME, exchange=TRANSLATION_EXCHANGE, routing_key=TRANSLATION_ROUTING_KEY)
        self.consumer_channel.basic_qos(prefetch_count=1)
        self.consumer_channel.basic_consume(TRANSLATION_QUEUE_NAME, on_message_callback=self.callback)

        self.consumer_channel.start_consuming()


rabbit_mq = Rabbit()
