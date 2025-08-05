from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from app.voice_handler import handle_voice
import requests
from logger import logger

user_router = Router()

@user_router.message(CommandStart())
async def welcome(message: Message):
    # response = requests.get('https://randomfox.ca/floof/')
    # cat = response.json()['link']
    logger.info(f'User {message.from_user.id} started bot')
    # await message.answer('Привет, я готов к работе, а пока держи фото лисички!')
    # await message.answer_photo(cat, has_spoiler = False)
    await message.answer("Привет! Я голосовой помощник для суммаризации голосовых сообщений")
@user_router.message(F.voice)
async def generating_voice(message: Message):
    response = await handle_voice(message)
    logger.info("responsing")
    await message.answer(response)