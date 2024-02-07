from brain_games import functions
from brain_games.games import calc
from brain_games import game_logic


def main():
    game_logic.launch_game(
        calc.notice,
        functions.create_game_data(calc.question, calc.answer)
    )


if __name__ == '__main__':
    main()
