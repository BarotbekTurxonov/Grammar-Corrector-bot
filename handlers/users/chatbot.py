from aiogram import types
from loader import dp
import openai
from states.ChatState import ChatState
from aiogram.dispatcher import FSMContext
from data.gingerit import GingerIt
from python_translator import Translator


translator = Translator()


@dp.message_handler(commands='chatbot', state='*')
async def chatbot(msg: types.Message):
	await msg.answer('Hello, Let\'s talk with me!')

	await ChatState.text.set()


@dp.message_handler(state=ChatState.text)
async def chatstt(msg: types.Message, state : FSMContext):
	data = msg.text
	print(data)
	data = data.capitalize()
    

	if data == "/quit":
		await msg.answer('Chat was Cancelled')
		await state.finish()
	else:
		text = await GingerIt().parse(msg.text)
		res = text['result']
		if len(text['corrections']) == 0:
			pass
		elif text['result'] == text['text'] or text['result'].lower() == text['text'].lower():
			return None
		else:
			for num in range(len(text['corrections'])):
				res = res.replace(text['corrections'][num]['correct'], f"<u>{text['corrections'][num]['correct']}</u>")
			await msg.reply(res)

		openai.api_key = "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"
		response = openai.Completion.create(
		  model="text-davinci-003",
		  prompt=data,
		  temperature=0,
		  max_tokens=60,
		  top_p=1.0,
		  frequency_penalty=0.0,
		  presence_penalty=0.0
		).choices[0].text

		
		await msg.reply(f"""<b>{response}</b>""")                
		# await msg.answer(openaidef(msg.text))


"""
import os
import openai


response = openai.Completion.create(
  model="code-davinci-002",
  prompt=
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\""]
)
"""
















