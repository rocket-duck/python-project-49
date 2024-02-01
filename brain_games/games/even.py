from brain_games import game_logic
from brain_games import functions
from random import randint

notice = 'Answer "yes" if the number is even, otherwise answer "no".'

min_number = 1
max_number = 100

def create_game_data():
    question = randint(min_number, max_number)
    if functions.is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question, correct_answer)

game_logic.game(notice, create_game_data())
