from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from app.voice_handler import handle_voice
from logger import logger

user_router = Router()

@user_router.message(CommandStart())
async def welcome(message: Message):

    logger.info(f'User {message.from_user.id} started bot')

    await message.answer("Привет! Я голосовой помощник для суммаризации голосовых сообщений.")
@user_router.message(F.voice)
async def generating_voice(message: Message):
    response = await handle_voice(message)
    logger.info("responding")
    await message.answer(response)
