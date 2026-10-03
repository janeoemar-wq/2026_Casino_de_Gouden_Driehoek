"""
****************    FUNCTIES IN BLACKJACK:
def create_deck():maak een deck aan van 52 kaarten
def draw_card: trek een kaart
def show_hand: laat je kaarten zien
def calculate_card_value: bereken de waarde kaartern
def calculate_hand_value bereken de waarde kaarten van je hand
def play_blackjack
"""
#-----------------------------------------------
import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def create_deck():
    deck = [f"{suit}{rank}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def draw_card(deck, hand):
    card = deck.pop()
    hand.append(card)
    return card

def show_hand(label, hand, hide_card=False):
    if hide_card:
        visible_cards = hand[:1] + ["??"]
    else:
        visible_cards = hand

    print(f"{label}: {' | '.join(visible_cards)}")

def calculate_card_value(card):
    rank = card[1:]

    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)

def calculate_hand_value(hand):
    total = 0
    number_of_aces = 0

    for card in hand:
        total += calculate_card_value(card)
        if card[1:] == "A":
            number_of_aces += 1

    while total > 21 and number_of_aces > 0:
        total -= 10
        number_of_aces -= 1

    return total

def play_blackjack(balance:float):
    opnieuw = "1"
    while opnieuw == "1":

        print("\n Casino de Gouden Driehoek - ♠ ♥ ♦ ♣   Blackjack   ♠ ♥ ♦ ♣")
        print("--------------------------------------")
        print(f"Huidig saldo: €{balance:.2f}")

        try:
            bet = float(input("Wat wil je inzetten? €"))
        except ValueError:
            print("Voer een geldig bedrag in.")
            continue

        if bet <= 0 or bet > balance:
            print("Ongeldige inzet.")
            continue
        print("Inzet geaccepteerd")

        balance -= bet

        deck = create_deck()

        player_hand = []
        dealer_hand = []

        draw_card(deck, player_hand)
        draw_card(deck, player_hand)

        draw_card(deck, dealer_hand)
        draw_card(deck, dealer_hand)

        show_hand("Jouw hand", player_hand)
        show_hand("Dealer toont", dealer_hand, True)

        print(f"Jouw totaal: {calculate_hand_value(player_hand)}")

        while calculate_hand_value(player_hand) < 21:

            choice = input("\nKies 1 = hit of 0 = stand: ")

            if choice == "0":
                break
            if choice != "1":
                print("Kies 1 voor Hit of 0 voor stand.")
                continue

            card = draw_card(deck, player_hand)

            print(f"Je trekt: {card}")

            show_hand("Jouw hand", player_hand)

            player_total = calculate_hand_value(player_hand)

            print(f"Jouw totaal: {player_total}")
        player_total = calculate_hand_value(player_hand)

        if player_total > 21:
            print("Bust! Je bent boven de 21.")
            print(f"Nieuw saldo: €{balance:.2f}")
            opnieuw = input ("\nWil je opnieuw spelen? Ja = 1, Nee = 0:")
            if opnieuw == "0":
                return balance #hiermee stop je de functie
            continue           #hiermee ga je terug naar while opnieuw ==1

        print("\nDealer is aan de beurt.")

        show_hand("Dealer hand", dealer_hand)

        while calculate_hand_value(dealer_hand) < 17:
            card = draw_card(deck, dealer_hand)

            print(f"Dealer trekt: {card}")

            show_hand("Dealer hand", dealer_hand)

        player_total = calculate_hand_value(player_hand)
        dealer_total = calculate_hand_value(dealer_hand)

        print(f"\nJouw totaal: {player_total}")
        print(f"Dealer totaal: {dealer_total}")

        if dealer_total > 21:
            print("Dealer bust! Je wint.")
            balance += bet * 2

        elif player_total > dealer_total:
            print("Je wint van de dealer!")
            balance += bet * 2

        elif player_total == dealer_total:
            print("Gelijkspel.")
            balance += bet

        else:
            print("Dealer wint.")

        print(f"Nieuw saldo: €{balance:.2f}")

        opnieuw = input("\nOpnieuw spelen? Ja = 1, Nee = 0: ")

        if opnieuw == "0":
            return balance
    return balance
