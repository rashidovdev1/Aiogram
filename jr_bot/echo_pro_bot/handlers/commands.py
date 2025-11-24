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
    await message.answer("Komandalar: \n/start - Botni qayta ishga tushirish \n/info - ma'lumot \n/about - bot haqida \n/help - yordam") #\n/weather - havo haqida

@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.reply(
        f"ℹ️ <b>Sizning ma'lumotlaringiz:</b>\n\n"
        f"🇺🇿 Ism: {message.from_user.first_name}\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"👤 Username: @{message.from_user.username or 'sizda_username_yoq'}",
        parse_mode="HTML"
    )


@router.message(Command('about'))
async def cmd_about(message: Message):

    CREATOR_USERNAME = "tezzro"
    VERSION = "1.3.0"
    CREATED_DATE = "2025"

    await message.reply(
        f"🤖 <b>BOT HAQIDA</b>\n\n"
        f"📌 Nomi: Echo Bot\n"
        f"👤 Username: @{CREATOR_USERNAME}\n"
        f"📅 Yaratilgan: {CREATED_DATE}\n"
        f"🔢 Versiya: {VERSION}\n\n"
        f"💡 Bu bot <b>aiogram 3</b> kutubxonasi bilan yaratilgan.\n",
        parse_mode="HTML"
    )