
question = input("Скажи что-нибудь: ")

def get_answer(question):
	question = question.lower()
	answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	answer = answers.get(question, 'я тебя не понимать')
	return answer

print(get_answer(question))
