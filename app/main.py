from decouple import config
from fastapi import FastAPI
from app.configs.db.sqlite import Base, engine

from app.rabbitmq.rabbitmq_factory.consumer_factory import RabbitConsumerFactory
from app.rabbitmq.calbacks.rabbitmq_callback import callback
from app.routers import health, portfolio, student

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(portfolio.router)
app.include_router(student.router)
app.include_router(health.router)

# RabbitConsumerFactory(
#     queue=config('RABBITMQ_QUEUE'), 
#     callback=callback
# ).create_consumer()
