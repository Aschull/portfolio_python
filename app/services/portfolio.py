from app.rabbitmq.publisher import RabbitPublisher

class Portfolio:
    def create_message(self, message: str, queue_name: str):
        publisher = RabbitPublisher(
            body=(message),
            queue=queue_name, 
            exchange=(queue_name + '_EXACHANGE'), 
            routing_key=(queue_name + '_ROUTING_KEY'), 
        )
        print(publisher.body)
        publisher.publish()
