from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

inline_btn = InlineKeyboardMarkup(
	keyboard=[
		InlineKeyboardButton('Translition', callback_data='translation')
	]
)