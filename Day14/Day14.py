from art import logo
from gameData import data
import random

def get_random_account():
    return random.choice(data)

def show_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def compare_data(guess, choice_a, choice_b):
    if choice_a > choice_b:
        return guess == "a"
    else:
        return guess == "b"

def start_game():
    print(logo)
    score = 0
    continue_game = True

    account_a = get_random_account()
    account_b = get_random_account()

    while continue_game:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()


        print(f"Compare A: {show_data(account_a)}.")
        print("vs")
        print(f"Against B: {show_data(account_b)}.")


        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_user_correct = compare_data(guess, a_follower_count, b_follower_count)

        print("\n" * 50)
        print(logo)
        
        if is_user_correct:
            score += 1 
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")

start_game()