from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        f"Assalomu alaykum {message.from_user.first_name}!\n\n"
        f"Men oddiy Echo botman\n"
    )

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Komandalar: \n/start - Botni qayta ishga tushirish \n/info - ma'lumot \n/help - yordam") #\n/weather - havo haqida

@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.reply(
        f"ℹ️ <b>Sizning ma'lumotlaringiz:</b>\n\n"
        f"🇺🇿 Ism: {message.from_user.first_name}\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"👤 Username: @{message.from_user.username or 'sizda_username_yoq'}",
        parse_mode="HTML"
    )