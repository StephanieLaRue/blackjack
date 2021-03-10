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
    # validate input 
    while True:
        try:
            user_money = float(input("Starting money:\t"))

            if user_money < 0 or user_money > 10000:
                print("Invalid amount. Must be from 0 to 10,000.")
            else:
                break

        except ValueError:
            continue
    print()

    # Get bet amount -> input by user
    # continue until user exits
    # validate input 
    while True:
        try:
            bet_amount = input("Bet amount: ")
            
            if bet_amount.lower() == "x":
                break

            bet_amount = float(bet_amount)

            if bet_amount < 5:
                print("The minimum bet is 5.")
            elif bet_amount > 1000:
                print("The maximum bet is 1,000.")
            elif bet_amount > user_money:
                print("You don't have enough money to make that bet.")
            else:
                outcome = play_hand()
                if outcome == "b":
                    user_money += bet_amount * 1.5
                    print("BLACKJACK!")
                elif outcome == "w":
                    user_money += bet_amount
                    print("You're a winner!")
                elif outcome == "p":
                    print("No Change!")
                else:
                    user_money -= bet_amount
                    print("You lost!")

                print("Money:", round(user_money, 2))
                print()
        except ValueError:
            continue

    print("Goodbye, friend!")


if __name__ == "__main__":
    main()