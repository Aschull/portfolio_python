from fastapi import APIRouter
from app.schemas.message import Message

from app.services.portfolio import Portfolio

router = APIRouter()

portfolio = Portfolio()
@router.post("/message/{queue_name}")
def create_message(message: Message, queue_name: str):
    portfolio.create_message(message.message, queue_name)
    return {"message": {message.message}}