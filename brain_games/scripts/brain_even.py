from brain_games import functions
from brain_games.games import even
from brain_games import game_logic


def main():
    question = even.make_question()
    answer = even.make_answer(question)
    game_logic.launch_game(even.notice, functions.create_game_data(question, answer))


if __name__ == '__main__':
    main()
