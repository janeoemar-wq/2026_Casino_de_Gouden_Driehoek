"""
Table toevoegen standaard format als alle andere spellen
consitent is kleuren in spellen
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

    totaal = calculate_hand_value(hand)

    inhoud = (
        f"{' | '.join(visible_cards)}"
        f"{' ' * 10}"
        f"[bold yellow]Totaal: {totaal}[/bold yellow]"
    )

    console.print(
        Panel(
            inhoud,
            title=f"[bold white]{label}[/bold white]",
            border_style="bright_yellow",
            width=50
        ),
        justify="center"
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
    console.print(
        Panel(
            "[bold yellow]♠ ♥ ♦ ♣ BLACKJACK ♠ ♥ ♦ ♣[/bold yellow]",
            border_style="bright_yellow",
            width=50
        ),
        justify="center"
    )
    opnieuw = "1"
    while opnieuw == "1":
        try:
            bet = float(console.input("[bold white]Wat wil je inzetten? €[/bold white]"))
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
        while calculate_hand_value(player_hand) < 21:

            choice = console.input("\n[bold white]Kies 1 = hit of 0 = stand: [/bold white]")

            if choice == "0":
                break
            if choice != "1":
                console.print("[bold red]Kies 1 voor Hit of 0 voor stand.[/bold red]")
                continue

            card = draw_card(deck, player_hand)
            console.print(f"[bold white]Je trekt: {card}[/bold white]")

            show_hand("Jouw hand", player_hand)


        player_total = calculate_hand_value(player_hand)

        if player_total > 21:
            console.print(
                Panel(
                    f"[bold red]Bust! Je bent boven de 21.[/bold red]\n\n"
                    f"Huidig saldo: €{balance + bet:.2f}\n"
                    f"Inzet: €{bet:.2f}\n"
                    f"Resterend saldo: €{balance:.2f}",
                    title="[bold yellow]RESULTAAT[/bold yellow]",
                    border_style="red",
                    width=50
                ),
                justify="center"
            )
            opnieuw = console.input("\n[bold white]Opnieuw spelen? Ja = 1, Nee = 0: [/bold white]")
            if opnieuw == "0":
                return balance #hiermee stop je de functie
            continue           #hiermee ga je terug naar while opnieuw ==1

        console.print("\n[bold white]Dealer is aan de beurt.[/bold white]")
        oud_saldo = balance + bet

        show_hand("Dealer hand", dealer_hand)

        while calculate_hand_value(dealer_hand) < 17:
            card = draw_card(deck, dealer_hand)

            console.print(f"[bold white]Dealer trekt: {card}[/bold white]")

            show_hand("Dealer hand", dealer_hand)

        player_total = calculate_hand_value(player_hand)
        dealer_total = calculate_hand_value(dealer_hand)

        if dealer_total > 21:
            balance += bet * 2
            console.print(
                Panel(
                    f"[bold green]Je wint van de dealer![/bold green]\n\n"
                    f"Huidig saldo: €{oud_saldo:.2f}\n"
                    f"Inzet: €{bet:.2f}\n"
                    f"Resterend saldo: €{balance:.2f}",
                    title="[bold yellow]OUTPUT[/bold yellow]",
                    border_style="green",
                    width=50
                ),
                justify="center"
            )
        elif player_total > dealer_total:
            console.print("[bold green]Je wint van de dealer![/bold green]")
            balance += bet * 2

        if dealer_total > 21:

            balance += bet * 2

            console.print(
                Panel(
                    f"[bold green]Dealer bust! Je wint.[/bold green]\n\n"
                    f"Huidig saldo: €{oud_saldo:.2f}\n"
                    f"Inzet: €{bet:.2f}\n"
                    f"Resterend saldo: €{balance:.2f}",
                    title="[bold yellow]RESULTAAT[/bold yellow]",
                    border_style="green",
                    width=50
                ),
                justify="center"
            )

        elif player_total > dealer_total:
            balance += bet * 2
            console.print(
                Panel(
                    f"[bold green]Je wint van de dealer![/bold green]\n\n"
                    f"Huidig saldo: €{oud_saldo:.2f}\n"
                    f"Inzet: €{bet:.2f}\n"
                    f"Resterend saldo: €{balance:.2f}",
                    title="[bold yellow]OUTPUT[/bold yellow]",
                    border_style="green",
                    width=50
                ),
                justify="center"
            )

        elif player_total == dealer_total:
            balance += bet
            console.print(
                Panel(
                    f"[bold yellow]Gelijkspel.[/bold yellow]\n\n"
                    f"Huidig saldo: €{oud_saldo:.2f}\n"
                    f"Inzet: €{bet:.2f}\n"
                    f"Resterend saldo: €{balance:.2f}",
                    title="[bold yellow]OUTPUT[/bold yellow]",
                    border_style="bright_yellow",
                    width=50
                ),
                justify="center"
            )

        else:
            console.print(
                Panel(
                    f"[bold red]Dealer wint.[/bold red]\n\n"
                    f"Huidig saldo: €{oud_saldo:.2f}\n"
                    f"Inzet: €{bet:.2f}\n"
                    f"Resterend saldo: €{balance:.2f}",
                    title="[bold red]RESULTAAT[/bold red]",
                    border_style="red",
                    width=50
                ),
                justify="center"
            )
        opnieuw = console.input("\n[bold white]Opnieuw spelen? Ja = 1, Nee = 0: [/bold white]")

    if opnieuw == "0":
        return balance
    return balance

