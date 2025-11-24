from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Salom!, Men echo botman')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('/start - Botni ishga tushirish \n/help - Yordam')