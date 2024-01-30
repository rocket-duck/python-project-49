from random import randint
import prompt


def main():
    welcome_message = "Welcome to the Brain Games!"
    print(welcome_message)

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(game_rules)

    attempts_count = 3
    while attempts_count > 0:
        question_number = randint(1, 100)
        question = f'Question: {question_number}'
        print(question)

        answer = prompt.string('Your answer: ')
        if is_even(question_number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer == correct_answer:
            correct = 'Correct!'
            print(correct)
        else:
            failure = f'\"{answer}\" is wrong answer ;(. Correct answer was \"{correct_answer}\".\nLet\'s try again, {name}!'
            return failure
        attempts_count -= 1
    win = f'Congratulations, {name}!'
    return win

def is_even(num):
    return num % 2 == 0

if __name__ == '__main__':
    main()
