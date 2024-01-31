import brain_games.source as source


def main():
    print(source.welcome_message)
    name = source.get_name()
    print(source.greeting(name))

    game_annotation = 'What is the result of the expression?'
    print(game_annotation)

    while source.attempts_count > 0:
        number1 = source.get_number(1, 10)
        number2 = source.get_number(1, 10)
        symbols = ['+', '-', '*']
        symbol_index = source.get_number(0, 2)

        question = f'Question: {number1} {symbols[symbol_index]} {number2}'
        print(question)

        answer = source.get_answer()

        match symbols[symbol_index]:
            case '+':
                correct_answer = number1 + number2
            case '-':
                correct_answer = number1 - number2
            case '*':
                correct_answer = number1 * number2

        if answer != str(correct_answer):
            return print(source.failure_message(
                answer, correct_answer, name)
            )

        correct = 'Correct!'
        print(correct)
        source.attempts_count -= 1

    return source.win_message(name)


if __name__ == '__main__':
    main()
