import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    print(f"Take A Guess, What Is The Secret Number 1 - {difficulty}")
    user_guess = int(input())
    return user_guess


def compare_results(secret_number, user_guess):
    if user_guess == secret_number:
        a = True
        return a
    else:
        a = False
        return a


def play_guess_game(difficulty):
    n1 = generate_number(difficulty)
    n2 = get_guess_from_user(difficulty)
    wl = compare_results(n1, n2)
    if wl:
        print("You Won")
        return True
    else:
        print("You Lost")
        return False
