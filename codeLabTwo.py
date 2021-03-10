#! /usr/bin/env python3

print("BLACKJACK!")
print("Blackjack payout is 3:2")
print("Enter 'x' for bet to exit\n")

# Get starting money -> input from user
totalMoney = float(input("Starting money:\t  "))

# Calculate the play and display the result
# continue until user enters "x"
while True:
    # Get bet amount -> input by user
    bet_amount = input("\nBet amount: ")

    if bet_amount.lower() == "x":
        break

    bet_amount = float(bet_amount)

    # Get hand to play -> input by user
    play = input("Blackjack, win, push, or lose? (b/w/p/l): ")
    
    if play == "b":
        totalMoney += bet_amount * 1.5
    elif play == "w":
        totalMoney += bet_amount
    elif play == "l":
        totalMoney -= bet_amount
    else:
        totalMoney = totalMoney

    print("Money:", round(totalMoney, 2))

print("Goodbye, friend!")
