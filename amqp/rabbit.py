import pika
import json
from file_ops import download_file, clean_residual_files
from spaces import Spaces
import asyncio
from concurrent.futures import ProcessPoolExecutor
# from scripts.pipeline_ai import multi_process


class Rabbit:
    producer_channel: pika.adapters.blocking_connection.BlockingChannel = None
    POOL_EXCHANGE = 'pool'
    POOL_ROUTING_KEY = 'poolkey'

    space: Spaces

    def get_audio_type(self, language):
        if language == "hindi":
            return "_hi"
        elif language == "telugu":
            return "_tel"
        elif language == "bengali":
            return "_be"
        elif language == "assamese":
            return "_asm"
        elif language == "bodo":
            return "_bod"
        elif language == "gujrati":
            return "_guj"
        elif language == "kannada":
            return "_kan"
        elif language == "malyalam":
            return "_mal"
        elif language == "marathi":
            return "_mar"
        elif language == "manipuri":
            return "_mni"
        elif language == "odiya":
            return "_odi"
        elif language == "punjabi":
            return "_pan"
        elif language == "tamil":
            return "_tam"


    def callback(self, channel, method, properties, body):
        msg = json.loads(body)
        print(msg)
        print(msg["euid"])
        print(msg['link'])
        print(msg['language'])
        print(msg['email_id'])

        # download function
        extension = download_file(url=msg["link"], filename=f"/data/input{msg['euid']}")

        # multi_process(msg["input_dir"], msg["audioname"], msg["lang"])

        clean_residual_files(filename=msg['euid'], extension=extension)

        executor = ProcessPoolExecutor(len(msg['language']))
        loop = asyncio.get_event_loop()
        for lang in msg['language']:
            loop.run_in_executor(executor, self.space.upload(filepath=f"data/output/{msg['euid']}{self.get_audio_type(lang)}.{extension}", bucket_path="audio/output"))
        # publish function
        try:
            loop.run_forever()
        finally:
            loop.close()

        self.producer_channel.basic_publish(exchange=Rabbit.POOL_EXCHANGE, routing_key=Rabbit.POOL_ROUTING_KEY, body="translation done", )
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def __init__(self):
        RABBIT_URL = 'amqp://guest:guest@localhost:5672'

        TRANSLATION_ROUTING_KEY = 'translationkey'
        TRANSLATION_QUEUE_NAME = 'translation_pipeline'
        TRANSLATION_EXCHANGE = 'translation'

        POOL_QUEUE_NAME = 'update_pool'

        self.space = Spaces()

        self.connection = pika.BlockingConnection(pika.URLParameters(RABBIT_URL))

        self.producer_channel = self.connection.channel()
        self.producer_channel.queue_declare(queue=POOL_QUEUE_NAME, auto_delete=False, durable=True, arguments={'x-queue-type': 'quorum'})

        self.consumer_channel = self.connection.channel()
        self.consumer_channel.queue_declare(queue=TRANSLATION_QUEUE_NAME, auto_delete=False, durable=True, arguments={'x-single-active-consumer': True})
        self.consumer_channel.queue_bind(queue=TRANSLATION_QUEUE_NAME, exchange=TRANSLATION_EXCHANGE, routing_key=TRANSLATION_ROUTING_KEY)
        self.consumer_channel.basic_qos(prefetch_count=1)
        self.consumer_channel.basic_consume(TRANSLATION_QUEUE_NAME, on_message_callback=self.callback)

        print("Vaaani-ML starting to consume")

        self.consumer_channel.start_consuming()


rabbit_mq = Rabbit()
