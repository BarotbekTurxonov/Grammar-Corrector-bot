from aiogram import types
from loader import dp, bot
from data.config import ADMINS
from utils.db_api.baza import send_ex
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['cancel'], state="*")
async def cancel(msg: types.Message, state  : FSMContext):
    await state.finish()
    await msg.answer("Cancelled.")



class Advertising(StatesGroup):
    text = State()
    photo = State()
    caption = State()

# Command handler for admin menu
@dp.message_handler(commands='admin')
async def admin_menu(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton("Statistika 📊")], [types.KeyboardButton("Reklama Yuborish 📝")]], resize_keyboard=True)
    if msg.from_user.id in ADMINS:
        await msg.answer("Welcome to Admin Panel", reply_markup=keyboard)
    else:
        await msg.answer("You are not an admin.")

# Handler for displaying statistics
@dp.message_handler(text="Statistika 📊")
async def statis(msg: types.Message):
    users = send_ex("SELECT user_id FROM users")
    await msg.answer(f"Total {len(users)} users")

# Handler for initiating advertisement selection
@dp.message_handler(text="Reklama Yuborish 📝")
async def getsm(msg: types.Message, state: FSMContext):
    keybrd = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton("Rasmli 🖼", callback_data='photo')],
        [types.InlineKeyboardButton("Matnli 📝", callback_data='text')]
    ])
    await msg.answer("Qanday turdagi Reklama Yuborishni xoxlaysiz", reply_markup=keybrd)
    await Advertising.text.set()

# Handler for processing inline keyboard selections
@dp.callback_query_handler(text=['photo', 'text'], state=Advertising.text)
async def inline_selection(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    async with state.proxy() as data:
        data['selection'] = call.data

    if call.data == 'photo':
        await call.message.answer("Please send the image you want to use for the advertisement.")
        await Advertising.photo.set()
    else:
        await call.message.answer("Please send the text-based advertisement.")
        await Advertising.caption.set()

# Handler for receiving photo and caption
@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=Advertising.photo)
async def photo_received(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    async with state.proxy() as data:
        data['photo_id'] = photo_id
    await message.answer("Great! Now please send the caption for the image-based advertisement.")
    await Advertising.caption.set()

# Handler for receiving caption and sending advertisement
@dp.message_handler(state=Advertising.caption)
async def caption_received(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        selection = data['selection']

    if selection == 'photo':
        caption = message.text

        # Send the image-based advertisement with the provided caption to all users
        users = send_ex("SELECT user_id FROM users")
        for user in users:
            user_id = user[0]
            await bot.send_photo(user_id, photo=data['photo_id'], caption=caption)

        await message.answer("Advertisement sent to all users.")
        await state.finish()

    else:
        advertisement_text = message.text

        # Send the text-based advertisement to all users
        users = send_ex("SELECT user_id FROM users")
        for user in users:
            user_id = user[0]
            await bot.send_message(user_id, advertisement_text)

        await message.answer("Advertisement sent to all users.")
        await state.finish()
