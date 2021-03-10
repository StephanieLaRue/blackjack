#! /usr/bin/env python3

import random

FILENAME = "cash.txt"

def display_header():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

def starting_money():
    # Get starting money -> input from user
    # validate input 
    while True:
        try:
            user_money = float(get_money())
            print("Money:", round(user_money, 2))

            if user_money < 0 or user_money > 10000:
                print("Invalid amount. Must be from 0 to 10,000.")
            else:
                break

        except ValueError:
            continue
    print()
    return user_money

# Get hand to play -> input by user
# Calculate the play and display the result
def play_hand(deck):
    # create new hands for start of game
    dealers_hand = []
    players_hand = []
    outcome = ""

    add_card(players_hand, deal_cards(deck))
    add_card(players_hand, deal_cards(deck))

    add_card(dealers_hand, deal_cards(deck))
    show_hand(dealers_hand, "\nDEALER'S SHOW CARD: ")
    show_hand(players_hand, "\nYOUR CARDS: ")

    
    playing(players_hand, deck)

    # dealer less than 17, must hit
    while calc_points(dealers_hand) < 17:
        # check for player bust & only two cards dealt to dealer
        if len(dealers_hand) == 2 and calc_points(players_hand) > 21:
            break
        add_card(dealers_hand, deal_cards(deck))


    # get final play outcome and end game
    show_hand(dealers_hand, "\nDEALER'S CARDS: ")
    outcome = get_outcome(players_hand, dealers_hand)

    print("\nYOUR POINTS:\t", calc_points(players_hand))
    print("DEALER'S POINTS:", calc_points(dealers_hand))
    print()
        
    return outcome


# Create the deck and return the deck
def create_deck():
    deck = []
    ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"}
    suits = {"Hearts", "Spades", "Clubs", "Diamonds"}

    for suit in suits:
        for rank in ranks:
            if rank == "Ace":
                value = 11
            elif rank == "Jack" or rank == "Queen" or rank == "King":
                value = 10
            else:
                value = int(rank)

            deck.append([rank, suit, value])

    return deck

# Shuffle the deck in place
def shuffle_deck(deck):
    random.shuffle(deck)

# Deal cards and return a single card 
def deal_cards(deck):
    deal_card = deck.pop()
    return deal_card

# Add a card to a hand(player/comp)
def add_card(hand, card):
    hand.append(card)

# Show a hand(player/comp)
def show_hand(hand, title):
    print(title)
    for card in hand:
        print(card[0], "of", card[1])

# User hit - add cards to player hand and calc points
def playing(hand, deck):
    while True:
        try:
            hit_stand = input("\nHit or stand? (h/s): ")

            # validate hit or stand input
            if hit_stand.lower() != "h" and hit_stand.lower() != "s":
                print("\nInvalid entry. Hit or Stand? (h/s)")
            else:
                if hit_stand.lower() == "h":
                    # add cards to hand and return points
                    add_card(hand, deal_cards(deck))
                    player_points = calc_points(hand)
                    show_hand(hand, "\nYOUR CARDS: ")

                    # check for player bust
                    if player_points > 21:
                        print("\nYou Busted!")
                        break

                elif hit_stand.lower() == "s":
                    break
        except ValueError:
            continue


# Calc points, check for a dealer bust
# else - check for other win conditions
# return outcome
def get_outcome(players_hand, dealers_hand):
    dealer_points = calc_points(dealers_hand)
    player_points = calc_points(players_hand)

    if player_points > 21:
        return "l"
    if dealer_points > 21:
        print("\nDealer busted!")
        return "w"
    if player_points == 21 and len(players_hand) == 2:
        if dealer_points == 21 and len(dealers_hand) == 2:
            print("\nDealer has blackjack too.")
            return "p"
        else:
            return "b"
    elif player_points > dealer_points:
        return "w"
    elif dealer_points > player_points:
        return "l"
    elif player_points == dealer_points:
        return "p"
    print("Invalid Outcome")
    return "p"

# Calculate points based on current hand
# track aces and calc points based on num of aces
def calc_points(hand):
    points = 0
    aces = 0
    for card in hand:
        if card[0] == "Ace":
            aces += 1
        points += card[2]
    
    if aces > 0 and points > 21:
        points = points - (aces * 10)
    if aces > 1 and points <= 11:
        points += 10
    return points

# Calc & Display game results
# return updated player money amount
def get_results(result, bet, money):
    if result == "b":
        money += bet * 1.5
        print("BLACKJACK!")
    elif result == "w":
        money += bet
        print("You're a winner!")
    elif result == "p":
        print("No Change!")
    elif result == "l":
        money -= bet
        print("You lost!")
    print("Money:", round(money, 2))
    print()
    update_money_file(money)

# stop or continue game
def continue_game():
    while True:
        try:
            play = input("Play again? (y/n): ")

            if play.lower() != "y" and play.lower() != "n":
                print("\nInvalid Choice.")
            elif play.lower() == "y":
                return True
            else:
                return False
        except ValueError:
            continue

# Get money amount from file
def get_money():
    money = 0
    try:
        with open(FILENAME, "r") as file:
            money = file.read()
        file.close()
        return money
    except FileNotFoundError:
        print("Data file missing, resetting starting amount to 1000")
    return 1000

# Update winnings file
def update_money_file(money):
    with open(FILENAME, "w") as file:
        file.write(str(money))
    file.close()

# add more money to user pot
def buy_chips():
    buy = input("Would you like to buy more chips? (y/n): ")
    if buy.lower() == "y":
        amount = input("Amount: ")
        with open(FILENAME, "w") as file:
            file.write(str(amount))
        file.close()
        return True
    return False

def main():
    display_header()

    # Get bet amount -> input by user
    # continue until user exits
    # validate input 
    while True:
        deck = create_deck()
        shuffle_deck(deck)
        player_money = starting_money()

        if player_money < 5:
            print("You are out of money!")
            if not buy_chips():
                break
        try:
            bet_amount = float(input("Bet amount: "))
        except ValueError:
            print("Invalid amount, try again!")
            continue

        if bet_amount < 5:
            print("The minimum bet is 5.")
        elif bet_amount > 1000:
            print("The maximum bet is 1,000.")
        elif bet_amount > player_money :
            print("You don't have enough money to make that bet.")
        else:
            outcome = play_hand(deck)
            get_results(outcome, bet_amount, player_money)
            if not continue_game():
                break
    print("Goodbye, friend!")


if __name__ == "__main__":
    main()