"""
print vervangen door console.print
huidige saldo vervangen
"""
import random

from rich.console import Console
from rich.panel import Panel
console = Console()

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

    console.print(
        Panel(
            "|".join(visible_cards),
            title=label,
            border_style="cyan",
            width=50
        )
    )



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
        console.print(
            Panel(
                "[bold red]♠ ♥ ♦ ♣ BLACKJACK ♠ ♥ ♦ ♣[/bold red]",
                title="[bold yellow]CASINO DE GOUDEN DRIEHOEK[/bold yellow]",
                border_style="yellow",
                width=50
            )
        )

        try:
            bet = float(console.input("[bold cyan]Wat wil je inzetten? €[/bold cyan]"))
        except ValueError:
            console.print("[bold red]Voer een geldig bedrag in.[/bold red]")
            continue

        if bet <= 0 or bet > balance:
            console.print("[bold red]Ongeldige inzet.[/bold red]")
            continue
        console.print("[bold green]✓ Inzet geaccepteerd[/bold green]")
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

        console.print(f"[bold yellow]Jouw totaal: {calculate_hand_value(player_hand)}[/bold yellow]")

        while calculate_hand_value(player_hand) < 21:

            choice = console.input("\n[bold cyan]Kies 1 = hit of 0 = stand: [/bold cyan]")

            if choice == "0":
                break
            if choice != "1":
                console.print("[bold red]Kies 1 voor Hit of 0 voor stand.[/bold red]")
                continue

            card = draw_card(deck, player_hand)
            console.print(f"[bold cyan]Je trekt: {card}[/bold cyan]")

            show_hand("Jouw hand", player_hand)

            player_total = calculate_hand_value(player_hand)

            console.print(f"[bold yellow]Jouw totaal: {player_total}[/bold yellow]")
        player_total = calculate_hand_value(player_hand)

        if player_total > 21:
            console.print(
                Panel(
                    f"[bold red]Bust! Je bent boven de 21.[/bold red]\n\n"
                    f"[bold cyan]Nieuw saldo: €{balance:.2f}[/bold cyan]",
                    title="Output",
                    border_style="red",
                    width=50
                )
            )
            opnieuw = console.input("\n[bold cyan]Opnieuw spelen? Ja = 1, Nee = 0: [/bold cyan]")
            if opnieuw == "0":
                return balance #hiermee stop je de functie
            continue           #hiermee ga je terug naar while opnieuw ==1

        console.print("\n[bold cyan]Dealer is aan de beurt.[/bold cyan]")

        show_hand("Dealer hand", dealer_hand)

    while calculate_hand_value(dealer_hand) < 17:
        card = draw_card(deck, dealer_hand)

        console.print(f"[bold cyan]Dealer trekt: {card}[/bold cyan]")

        show_hand("Dealer hand", dealer_hand)

    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    console.print(f"\n[bold yellow]Jouw totaal: {player_total}[/bold yellow]")
    console.print(f"[bold yellow]Dealer totaal: {dealer_total}[/bold yellow]")

    if dealer_total > 21:
        console.print("[bold green]Dealer bust! Je wint.[/bold green]")
        balance += bet * 2

    elif player_total > dealer_total:
        console.print("[bold green]Je wint van de dealer![/bold green]")
        balance += bet * 2

    elif player_total == dealer_total:
        console.print("[bold yellow]Gelijkspel.[/bold yellow]")
        balance += bet

    else:
        console.print("[bold red]Dealer wint.[/bold red]")

    console.print(f"[bold green]Nieuw saldo: €{balance:.2f}[/bold green]")

    opnieuw = console.input("\n[bold cyan]Opnieuw spelen? Ja = 1, Nee = 0: [/bold cyan]")

    if opnieuw == "0":
        return balance
    return balance

