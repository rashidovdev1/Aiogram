# echo plus bot

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "8470618802:AAGK1g0j4j4PI3KO3DVjR9nk6LEIbK6eZ5k"
bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Assalomu alekum!. Men echo botman")

@dp.message()
async def echo(message: types.Message):
    await message.copy_to(chat_id=message.chat.id)


async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
