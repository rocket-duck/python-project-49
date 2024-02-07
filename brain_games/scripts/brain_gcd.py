from brain_games import functions
from brain_games.games import gcd
from brain_games import game_logic


def main():
    game_logic.launch_game(
        gcd.notice,
        functions.create_game_data(gcd.question, gcd.answer)
    )


if __name__ == '__main__':
    main()
