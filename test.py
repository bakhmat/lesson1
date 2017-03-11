
first_input = input("Say soomething: ")
second_input = input("Say something else: ")


def get_summ(something, something_else):
	something = str(something)
	something_else = str(something_else)
	sum_string = something + something_else
	return sum_string.upper()


xxx = get_summ(first_input, second_input)
print (xxx)
