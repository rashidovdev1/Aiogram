import asyncio
from aiogram import Bot, Dispatcher

from config.settings import BOT_TOKEN
from handlers import commands, messages

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(messages.router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())