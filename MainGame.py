import MemoryGame
import GuessGame
import CurrencyRouletteGame
import game_dep

list_of_games = ['MemoryGame', 'GuessGame', 'CurrencyRouletteGame']

while True:
    print("list of games: ")
    for i in range(len(list_of_games)):
        print(i, "-", list_of_games[i])
    try:
        choice = int(input(f"select your game: 0-{len(list_of_games) - 1})"))
        if 0 <= choice < len(list_of_games):
            break
        else:
            print("select from list, chosen option does not exist")
    except ValueError:
        print("Wrong Value")

diff = game_dep.get_difficulty()

if choice == 0:
    MemoryGame.play(diff)
elif choice == 1:
    GuessGame.play(diff)
else:
    CurrencyRouletteGame.play(diff)
