import random
import requests


def generate_money():
    money = random.randint(1, 101)
    print(f"{money}$")
    return money


def get_rate_by_api():
    response = (requests.get(
        "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_rjy6VUsvjANlvL5o9NhV0pNSb1s0lRRBj0DxYB0e&currencies=ILS"))
    rate = response.json()
    return rate


def get_money_interval(rate, difficulty):
    return rate - float(5 - difficulty), rate + float(5 - difficulty)


def get_guess_from_user():
    print("Enter Your Guess: ")
    guess = float(input())
    return guess


def play_currency_game(difficulty):
    usd = generate_money()
    rate = get_rate_by_api()
    inter = get_money_interval(rate, difficulty)
    user = get_guess_from_user()
    user1 = user
    user *= inter[0]
    user1 *= inter[1]
    if float(usd) >= user or float(usd) <= user:
        print(" You Won! ")
        return True
    else:
        print("You Lost")
        return False
