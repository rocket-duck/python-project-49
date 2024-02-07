import random
from brain_games import game_logic

notice = 'What is the result of the expression?'

game_symbols = ['+', '-', '*']

MIN_NUMBER = 1
MAX_NUMBER = 10


def make_question_and_answer():
    symbol = random.choice(game_symbols)
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f'{num1} {symbol} {num2}'

    match symbol:
        case '+':
            answer = num1 + num2
        case '-':
            answer = num1 - num2
        case '*':
            answer = num1 * num2

    return question, str(answer)


def run_game():
    game_logic.launch_game(notice, make_question_and_answer)
