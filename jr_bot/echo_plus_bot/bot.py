# echo plus bot

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import asyncio

BOT_TOKEN = "8470618802:AAGK1g0j4j4PI3KO3DVjR9nk6LEIbK6eZ5k"
bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Assalomu alekum!. Men echo botman")

@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer("Men echo botman. \nSizga yuborgan har qanday xabaringizni qaytaraman.\n📝 Komandalar: \n/start - Botni qayta ishga tushirish \n/info - malumot \n/weather - havo haqida")

@dp.message(Command('info'))
async def cmd_info(message: types.Message):
    await message.reply(
        f"ℹ️ <b>Sizning ma'lumotlaringiz:</b>\n\n"
        f"👤 Ism: {message.from_user.first_name}\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"👤 Username: @{message.from_user.username or 'sizda_username_yoq'}",
        parse_mode="HTML"
    )
@dp.message(Command('weather'))
async def cmd_weather(message: types.Message):
    await message.reply("🌤 Bugun ob-havo yaxshi!")

@dp.message(lambda msg: msg.text and msg.text.lower() in ['salom', 'assalom', 'assalomu alaykum'])
async def salom_txt(message: types.Message):
    await message.reply("✋🏻Vaalaykum assalom! Qalaysiz?")

@dp.message(lambda msg: msg.text and msg.text.lower() in ['raxmat','rahmat', 'thanks', 'thank you'])
async def raxmat_txt(message: types.Message):
    await message.reply("Arzimaydi🤝")

@dp.message(F.text.regexp(r'^\d+$'))
async def calculate_handler(message: types.Message):

    number = int(message.text)
    result = number * 2
    await message.reply(
        f"🔢 Hisoblash:\n"
        f"✖️ {number} × 2 = <b>{result}</b>",
        parse_mode="HTML"
    )

@dp.message()
async def echo(message: types.Message):
    await message.copy_to(chat_id=message.chat.id)

async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
