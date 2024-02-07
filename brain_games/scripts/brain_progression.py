from brain_games import functions
from brain_games.games import progression
from brain_games import game_logic


def main():
    game_logic.launch_game(
        progression.notice,
        functions.create_game_data(progression.question, progression.answer)
    )


if __name__ == '__main__':
    main()
