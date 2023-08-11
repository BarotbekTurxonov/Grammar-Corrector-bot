import openai

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

while True:
	a = input('Str > >  ')

	response = openai.Completion.create(
	  model="text-davinci-003",
	  prompt=a,
	  temperature=0.9,
	  max_tokens=150,
	  top_p=1,
	  frequency_penalty=0,
	  presence_penalty=0.6,
	  stop=[" Human:", " AI:"]
	)

	print(response.choices[0].text)






