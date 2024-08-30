import asyncio
import logging
import os

from aiogram import *
from dotenv import load_dotenv

from app.main_handler import router

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(message)s')
    logging.log(level=logging.ERROR, msg='Starting Bot...')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.log(level=logging.ERROR, msg='Exit...')
