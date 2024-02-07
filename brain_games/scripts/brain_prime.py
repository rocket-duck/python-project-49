from brain_games import functions
from brain_games.games import prime
from brain_games import game_logic


def main():
    game_logic.launch_game(
        prime.notice,
        functions.create_game_data(prime.question, prime.answer)
    )


if __name__ == '__main__':
    main()
