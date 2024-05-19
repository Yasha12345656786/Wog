import random


def generate_sequence(difficulty):
    lst = []
    while difficulty > 0:
        n = random.randint(1, 101)
        lst.append(n)
        difficulty -= 1
    return lst


def get_list_from_user(difficulty):
    guess = []
    print("Enter Each Number By The Order You Remember: ")
    for i in range(difficulty):
        print(f"Enter Your {i + 1} Guess:")
        guess.append(int(input()))
    list(guess)
    return guess


def is_list_equal(gen_lst, user_lst):
    gen_lst.sort()
    user_lst.sort()
    if user_lst == gen_lst:
        return True
    else:
        return False


def play_memory_game(difficulty):
    gen_lst = generate_sequence(difficulty)
    user_lst = get_list_from_user(difficulty)
    if is_list_equal(gen_lst,user_lst):
        print("You Won")
        return True
    else:
        print("You Lost")
        return False


