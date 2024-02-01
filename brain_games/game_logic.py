import prompt


def game(game_notice, game_data):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_notice)

    attempts_count = 3
    def game_progress(data, attempts):
        if attempts == 0:
            print(f'Congratulations, {name}!')
            return

        (question, correct_answer) = data

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if correct_answer != user_answer:
            print(f'\"{user_answer}\" is wrong answer ;(. '
            f'Correct answer was \"{correct_answer}\".'
            f'\nLet\'s try again, {name}!')
            return

        print('Correct!')

        return game_progress(data, attempts - 1)

    game_progress(game_data, attempts_count)
