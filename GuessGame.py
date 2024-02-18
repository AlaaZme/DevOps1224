import random
import game_dep


def play(difficulty):
    print("Game Description:\n"
          "Guess the number between 1 - and Difficulty you entered")
    secret_number = generate_number(difficulty)
    compare_results(get_guess_from_user(), secret_number)


def generate_number(diff):
    return random.randint(1, diff)


def get_guess_from_user():
    return game_dep.get_int("Guess The Number: ")


def compare_results(secret, user_num):
    if secret == user_num:
        print("True")
    else:
        print("False")
