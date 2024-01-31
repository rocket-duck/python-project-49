import brain_games.source as source


def main():
    print(source.welcome_message)
    name = source.get_name()
    print(source.greeting(name))

    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(game_rules)

    while source.attempts_count > 0:
        number = source.get_number(1, 100)
        question = f'Question: {number}'
        print(question)

        answer = source.get_answer()
        if source.is_even(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer != correct_answer:
            return print(source.failure_message(answer, correct_answer, name))

        correct = 'Correct!'
        print(correct)
        source.attempts_count -= 1

    return source.win_message(name)


if __name__ == '__main__':
    main()
