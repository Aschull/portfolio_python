from app.rabbitmq.rabbitmq_basic_client import RabbitMQClient


class RabbitConsumer(RabbitMQClient):
    def __callback(self, ch, method, properties, body):
        self.callback(body)

    def basic_consume(self):
        self.channel.basic_consume(
            queue=self.queue,
            on_message_callback=self.__callback,
            auto_ack=True
        )

    def consume(self):
        self.basic_consume()
        self.channel.start_consuming()
