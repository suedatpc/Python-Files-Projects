import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
answer = random.randint(1 , 100)
print(f"pssst the number is {answer}")

EASY_LVL_ATTEMPTS = 10
HARD_LVL_ATTEMPTS = 5

def compare_numbers(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1 
    else:
        print(f"You got it! The answer was {answer}.")


def choose_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LVL_ATTEMPTS
    else:
        return HARD_LVL_ATTEMPTS


def start_game():
    turns = choose_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = compare_numbers(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

start_game()
