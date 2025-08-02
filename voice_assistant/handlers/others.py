from aiogram.types import Message
from aiogram import Router, F
from app.generating import generating
from logger import logger
from prompts import prompt_text

router = Router()

other_router = Router()

@other_router.message(F.photo | F.document | F.sticker | F.video | F.caption)
async def others_handler(message: Message):
    await message.answer('Извините, на данный момент я могу обрабатывать только голосовые сообщения')

@other_router.message()
async def generating_text(message: Message):
    response = await generating(message.text, prompt_text, message.from_user.id)
    await message.answer(response)