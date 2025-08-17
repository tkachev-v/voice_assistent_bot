from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os
from logger import logger
from handlers.user import user_router
from handlers.others import other_router
from dotenv import load_dotenv

load_dotenv()
token_tg = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(token=token_tg)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(user_router)
    dp.include_router(other_router)
    try:
        logger.info('Starting Voice Assistant...')
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical('Could not start Voice Assistant.:%s®',e)

if __name__ == "__main__":
    asyncio.run(main())

