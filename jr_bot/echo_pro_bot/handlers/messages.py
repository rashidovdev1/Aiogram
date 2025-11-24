from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo(message: Message):
    try:
        await message.copy_to(chat_id=message.chat.id)
    except Exception as e:
        await message.reply("Kechirasiz bu xabarni qaytara olamdim")