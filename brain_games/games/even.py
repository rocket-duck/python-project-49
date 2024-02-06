from random import randint

notice = 'Answer "yes" if the number is even, otherwise answer "no".'

min_number = 1
max_number = 100


def is_even(num):
    return num % 2 == 0


def make_question():
    question = randint(min_number, max_number)
    return question


def make_answer(question):
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return answer
