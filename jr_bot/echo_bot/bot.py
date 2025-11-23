# echo bot

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "bot_token"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Salom! men echo botman")

@dp.message()
async def cmd_echo(message: types.Message):
    await message.copy_to(chat_id=message.chat.id)

async def main():
    print('Bot ishga tushdi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())