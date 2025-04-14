from brain_games.cli import welcome_user
from brain_games.games.prime import prime_game


def main():
    user_name = welcome_user()
    prime_game(user_name)


if __name__ == "__main__":
    main()