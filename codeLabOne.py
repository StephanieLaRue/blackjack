#! /usr/bin/env python3

print("BLACKJACK!")
print("Blackjack payout is 3:2\n")

# Get starting money and bet amount -> input from user
startingVal = float(input("Starting money:\t  "))
betAmount = float(input("Bet amount:\t  "))

# Calculate blackjack, win, push, and lose totals 
blackjack = round(startingVal + (betAmount * 1.5), 2)
winTotal = startingVal + betAmount
pushTotal = startingVal
loseTotal = startingVal - betAmount

# Display the totals and round the amounts
print("\nENDING MONEY FOR A...")
print("Blackjack:\t ", blackjack, "\nWin:\t\t ", winTotal)
print("Push:\t\t ", pushTotal, "\nLose:\t\t ", loseTotal)
print("\nGoodbye, friend!")