from random import randint
from brain_games import game_logic

notice = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False

    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1

    return True


def make_question_and_answer():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(question) else 'no'

    return question, answer


def run_game():
    game_logic.launch_game(notice, make_question_and_answer)
