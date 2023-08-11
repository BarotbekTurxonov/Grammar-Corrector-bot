from aiogram.dispatcher.filters.state import State, StatesGroup

class CheckState(StatesGroup):
	text = State()
	
	