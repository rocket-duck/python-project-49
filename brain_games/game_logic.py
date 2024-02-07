import prompt


def launch_game(notice, game_data):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{notice}')

    attempts_count = 3

    def game_progress(attempts, data):
        if attempts == 0:
            print(f'Congratulations, {name}!')
            return

        question, answer = data()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if answer != user_answer:
            print(f'\"{user_answer}\" is wrong answer ;(. '
                  f'Correct answer was \"{answer}\".'
                  f'\nLet\'s try again, {name}!')
            return

        print('Correct!')

        return game_progress(attempts - 1, data)

    game_progress(attempts_count, game_data)
