import prompt
from random import randint

welcome_message = "Welcome to the Brain Games!"


def get_name():
    return prompt.string('May I have your name? ')


def greeting(name):
    return f'Hello, {name}!'


attempts_count = 3


def get_number(x, y):
    return randint(x, y)


def get_answer():
    return prompt.string('Your answer: ')


def failure_message(answer, correct_answer, name):
    return (f'\"{answer}\" is wrong answer ;(. '
            f'Correct answer was \"{correct_answer}\".'
            f'\nLet\'s try again, {name}!')


def win_message(name):
    return f'Congratulations, {name}!'


def is_even(num):
    return num % 2 == 0
