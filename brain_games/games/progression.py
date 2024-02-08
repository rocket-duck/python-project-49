from random import randint
from brain_games import game_logic

notice = 'What number is missing in the progression?'

PROGRESSIOM_LENGTH = 10

MIN_NUMBER = 1
MAX_NUMBER = 10


def make_progression(start, step, length):
    progression = [start]
    i = 1
    while i <= length:
        progression.append(progression[i - 1] + step)
        i += 1

    return progression


def make_question_and_answer():
    progression_start = randint(MIN_NUMBER, MAX_NUMBER)
    progression_step = randint(MIN_NUMBER, MAX_NUMBER)

    make_question = make_progression(
        progression_start, progression_step, PROGRESSIOM_LENGTH
    )

    question_position = randint(MIN_NUMBER, MAX_NUMBER)

    answer = make_question[question_position]
    make_question[question_position] = '..'
    question = ' '.join(map(str, make_question))

    return question, str(answer)


def run_game():
    game_logic.launch_game(notice, make_question_and_answer)
