logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program.")

bids = {} #empty dictionary
is_bidding_finished = False
def clear():  # Prints 50 blank lines
    print("\n" * 50)


def find_the_highest(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not is_bidding_finished:
    name = input("What's your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    ask_to_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if ask_to_continue == "no":
        is_bidding_finished = True
        find_the_highest(bids)
    elif ask_to_continue == "yes":
        clear()


