from app.rabbitmq.rabbitmq_basic_client import RabbitMQClient

class RabbitPublisher(RabbitMQClient):
    def __init__(self, body, queue, exchange, routing_key):
        super().__init__(queue=queue, exchange=exchange, routing_key=routing_key, callback=None)
        self.body = body


    def publish(self):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=self.body
        )
        print(f'[x] - Sent message to: [{self.queue}] - {self.body}')
        self.connection.close()
