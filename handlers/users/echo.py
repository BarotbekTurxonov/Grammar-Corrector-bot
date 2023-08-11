from aiogram import types
from aiogram.types import ContentTypes
from loader import dp
from data.gingerit import GingerIt
from states.check import CheckState
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter



@dp.message_handler(chat_id=-1001619273446, commands='check')
async def correct_func(message: types.Message):
    args = message.get_args()

    text = GingerIt().parse(args)

    res = text['result']
    if len(text['corrections']) == 0:
        await message.reply("✅")
    elif text['result'] == text['text'] or text['result'].lower() == text['text'].lower():
        return None
    else:
        for num in range(len(text['corrections'])):
                res = res.replace(text['corrections'][num]['correct'], f"<u>{text['corrections'][num]['correct']}</u>")
        await message.reply(res)






@dp.message_handler(commands='check')
async def correct_func111(message: types.Message):
    args = message.get_args()

    text = GingerIt().parse(args)

    res = text['result']
    if len(text['corrections']) == 0:
        await message.reply("✅")
    elif text['result'] == text['text'] or text['result'].lower() == text['text'].lower():
        return None
    else:
        for num in range(len(text['corrections'])):
                res = res.replace(text['corrections'][num]['correct'], f"<u>{text['corrections'][num]['correct']}</u>")
        await message.reply(res)


