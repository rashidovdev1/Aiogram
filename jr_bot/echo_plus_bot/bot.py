# echo plus bot

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "TOKEN"
bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Assalomu alekum!. Men echo botman")

@dp.message(Command('help'))
async def help(message: types.Message):
    await message.answer("Men echo botman. \nSizga yuborgan har qanday xabaringizni qaytaraman.\n📝 Komandalar: \n/start - Botni qayta ishga tushirish \n/help - Yordam")

@dp.message()
async def echo(message: types.Message):
    await message.copy_to(chat_id=message.chat.id)


async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
