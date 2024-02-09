import threading

from app.rabbitmq.consumer import RabbitConsumer

class RabbitConsumerFactory:
    def __init__(self, queue, callback):
        self.queue = queue
        self.callback = callback

    def create_consumer(self):
        queue = self.queue.split(",")

        for item in queue:
            rabbit_consume = RabbitConsumer(
                queue=item, 
                exchange=item + '_EXCHANGE', 
                routing_key=item + '_ROUTING_KEY', 
                callback=self.callback
            )
            consumer = threading.Thread(target=rabbit_consume.consume)
            consumer.start()
            print(f'Consuming {item}.')
