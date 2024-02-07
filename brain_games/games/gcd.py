from random import randint
from brain_games import game_logic


notice = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def find_GCD(num_1, num_2):
    if num_2 > num_1:
        return find_GCD(num_2, num_1)

    if num_2 == 0:
        return num_1

    return find_GCD(num_2, num_1 % num_2)


def make_question_and_answer():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)

    question = f'{num1} {num2}'
    answer = find_GCD(num1, num2)

    return question, str(answer)


def run_game():
    game_logic.launch_game(notice, make_question_and_answer)
