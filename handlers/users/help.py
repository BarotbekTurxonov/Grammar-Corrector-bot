from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Server haqida ma'lumot beradi",
            "/check Your Message Here")
    
    await message.answer("\n".join(text))
