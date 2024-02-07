import prompt
from brain_games import functions


def launch_game(notice, game_data):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(notice)

    attempts_count = 3

    def game_progress(attempts, data):
        if attempts == 0:
            print(f'Congratulations, {name}!')
            return

        question = functions.get_question(data)
        answer = str(functions.get_answer(data))

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
