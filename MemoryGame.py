import os
from time import sleep
import random


def play(difficulty):
    print(
        "    Game description:\n "
        "The purpose of memory game is to display an amount of random numbers to the users for 0.7\n"
        " seconds and then prompt them from the user for the numbers that he remember. \n"
        "If he was right with all the numbers the user will win otherwise he will lose.\n\n\n")

    secret_list = generate_sequence(difficulty)
    input("Press enter to start: will display a list REMEMBER IT\n")

    print(secret_list)
    sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    user_list = get_list_from_user()
    is_list_equal(secret_list, user_list)


def generate_sequence(size):
    secret_list = []
    for _ in range(size):
        secret_list.append(random.randint(1, 101))
    return secret_list


def get_list_from_user():
    while True:
        input_str = input("Enter your list: ").strip()
        res = input_str.split(' ')
        num_list = list(filter(None, res))
        try:
            for num in num_list:
                int(num)
            return num_list
        except ValueError:
            print("illegal Value re try")


def is_list_equal(secret_list, user_list):
    if len(secret_list) == len(user_list):
        for i in range(len(secret_list)):
            if int(user_list[i]) != secret_list[i]:
                print("FALSE")
                break
        else:
            print("TRUE")

    else:
        print("False")
