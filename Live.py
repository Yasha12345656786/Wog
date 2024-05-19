
def ask_for_name():
    print("Enter Your Name:")
    name = str(input())
    if len(name) < 2:
        print("Invalid")
    else:
        return name


def welcome(name):
    print(f"Hello {name}, Welcome To The World Of Games(WoG). "
          f"Here You Can Find Many Cool Games To Play")


def choose_game():
    print("Please choose a game to play:1. Memory Game - a sequence of numbers will appear for 1 second and you have "
          "to guess it back 2. Guess Game - guess a number and see if you chose like the computer 3. Currency "
          "Roulette - try and guess the value of a random amount of USD in ILS)")
    gameChoice = int(input())
    if gameChoice == 1:
        print("Memory Game, Great Choice")
    elif gameChoice == 2:
        print("Guess Game, Great Choice")
    elif gameChoice == 3:
        print("Currency Roulette, Great Choice")
    else:
        print("Invalid Choice, Please Try Again")
    return gameChoice


def choose_difficulty():
    print("Please Choose Game Difficulty From 1 to 5")
    difficultyLvl = int(input())
    if difficultyLvl == 1:
        print("Difficulty Choosen: Easy")
    elif difficultyLvl == 2:
        print("Difficulty Choosen: Normal")
    elif difficultyLvl == 3:
        print("Difficulty Choosen: Hard")
    elif difficultyLvl == 4:
        print("Difficulty Choosen: Advanced")
    elif difficultyLvl == 5:
        print("Difficulty Choosen: Expert")
    return difficultyLvl


def load_game():
    difficulty = choose_difficulty()
    game = choose_game()
    if game == 1:
        print(f"{game} , Difficulty {difficulty}")
        from GuessGame import play_guess_game
        return play_guess_game(difficulty)
    elif game == 2:
        print(f"{game} , Difficulty {difficulty}")
        from MemoryGame import play_memory_game
        return play_memory_game(difficulty)
    elif game == 3:
        print(f"{game} , Difficulty {difficulty}")
        from CurrencyRouletteGame import play_currency_game
        return play_currency_game(difficulty)

    print("Your Game Is Loading...")


load_game()



