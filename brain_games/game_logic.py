import prompt


def launch_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.notice)

    attempts_count = 3

    def game_progress(attempts, gamef):
        if attempts == 0:
            print(f'Congratulations, {name}!')
            return

        question, answer = gamef.create_game_data()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if answer != user_answer:
            print(f'\"{user_answer}\" is wrong answer ;(. '
                  f'Correct answer was \"{answer}\".'
                  f'\nLet\'s try again, {name}!')
            return

        print('Correct!')

        return game_progress(attempts - 1, gamef)

    game_progress(attempts_count, game)
