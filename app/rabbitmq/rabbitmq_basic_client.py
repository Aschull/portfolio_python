import pika
from decouple import config

class RabbitMQClient:
    def __init__(self, queue: str, exchange: str, routing_key: str, callback):
        self.host = config('RABBITMQ_HOST')
        self.port = config('RABBITMQ_PORT')
        self.username = config('RABBITMQ_USERNAME')
        self.password = config('RABBITMQ_PASSWORD')
        self.virtual_host = config('RABBITMQ_VIRTUAL_HOST')
        self.queue = queue
        self.exchange = exchange
        self.routing_key = routing_key
        self.callback = callback
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host,
                port=self.port
            )
        )
        self.channel = self.connection.channel()
        
        # Declara queue, exchange, routing_key e faz o bind
        self.channel.queue_declare(queue=self.queue, durable=True)
        self.channel.exchange_declare(self.exchange)
        self.channel.queue_bind(
            queue=self.queue, 
            exchange=self.exchange, 
            routing_key=self.routing_key
        )
        self.channel.basic_qos(prefetch_count=1)
