import game_dep
import random
from currency_converter import CurrencyConverter


def play(difficulty):
    print("Game Description:\n "
          "Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
          "max_difficulty = 5 -- guess the exact number")
    max_difficulty = 5
    guessed_number = get_guess_from_user()
    if difficulty > max_difficulty:
        difficulty = max_difficulty
    secret_amount_interval = get_money_interval(difficulty)
    if secret_amount_interval[0] <= guessed_number <= secret_amount_interval[1]:
        print("TRUE")
    else:
        print("FALSE")


def get_money_interval(difficulty):

    c = CurrencyConverter()
    amount_usd = random.randint(1, 100)
    amount_ils = c.convert(amount_usd, 'USD', 'ILS')

    secret_amount_interval = (amount_ils - (5 - difficulty),
                              amount_ils + (5 - difficulty))

    return secret_amount_interval


def get_guess_from_user():
    return game_dep.get_int("Enter Guessed amount: ")
