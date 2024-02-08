from random import randint
from brain_games import game_logic

notice = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(num):
    return num % 2 == 0


def make_question_and_answer():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(question) else 'no'

    return question, answer


def run_game():
    game_logic.launch_game(notice, make_question_and_answer)
