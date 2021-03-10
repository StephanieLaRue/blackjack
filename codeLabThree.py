#! /usr/bin/env python3

import random

def display_header():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit\n")

# Get hand to play -> input by user
# Calculate the play and display the result
def play_hand():

    # Randomize play outcome
    # return char for appropriate outcomes
    rand_num = random.randint(1,100)

    if rand_num > 95:
        return "b"
    elif rand_num > 58:
        return "w"
    elif rand_num > 49:
        return "p"
    else:
        return "l"


def main():
    display_header()

    # Get starting money -> input from user
    totalMoney = float(input("Starting money:\t"))

    # Get bet amount -> input by user
    # continue until user exits
    while True:
        bet_amount = input("\nBet amount: ")
        
        if bet_amount.lower() == "x":
            break

        bet_amount = float(bet_amount)
        outcome = play_hand()

        if outcome.lower() == "b":
            totalMoney += bet_amount * 1.5
            print("BLACKJACK!")
        elif outcome.lower() == "w":
            totalMoney += bet_amount
            print("You're a winner!")
        elif outcome.lower() == "p":
            print("No Change!")
        elif outcome.lower() == 'l':
            totalMoney -= bet_amount
            print("You lost!")

        print("Money:", round(totalMoney, 2))

    print("Goodbye, friend!")


if __name__ == "__main__":
    main()