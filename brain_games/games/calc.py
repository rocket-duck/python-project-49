from random import randint

notice = 'What is the result of the expression?'


game_symbols = ['+', '-', '*']
symbol_index = randint(0, 2)

min_number = 1
max_number = 10

number_1 = randint(min_number, max_number)
number_2 = randint(min_number, max_number)

question = f'{number_1} {game_symbols[symbol_index]} {number_2}'


match game_symbols[symbol_index]:
    case '+':
        answer = number_1 + number_2
    case '-':
        answer = number_1 - number_2
    case '*':
        answer = number_1 * number_2
