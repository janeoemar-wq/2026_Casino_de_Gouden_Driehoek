"""
prints= console.print
imports rich
bij def start de win regels omgezet naar table
Resterend saldo toegevoegd
resultaat in een Panel
winregels in een Table
rollen in een Table
Rich markup in diverse regels
vaste width=50
meerdere rondes achter elkaar , hersteld
random.choice() met 8 symbolen, geen round_number

"""
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from wcwidth import width

console = Console()

def determine_rolls():
    symbolen = list(emojij_symbolen.keys())

    rol1 = random.choice(symbolen)
    rol2 = random.choice(symbolen)
    rol3 = random.choice(symbolen)

    return rol1, rol2, rol3


def determine_payout(rol1, rol2, rol3, inzet):
    if rol1 == rol2 == rol3:
        return inzet * 3
    elif rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return inzet
    else:
        return 0

def start(balance):
    winregels_tabel = Table(title="🎰 Winregels Fruitmachine 🎰", style="bold, width=50")
    winregels_tabel.add_column("Prijs", style="bold")
    winregels_tabel.add_column("Voorbeelden", style="bold")

    winregels_tabel.add_row(
        "Grote prijs (3x inzet)",
        "🍒🍒🍒  |  🍋🍋🍋  |  ⭐⭐⭐"
    )
    winregels_tabel.add_row(
        "Kleine prijs (inzet terug)",
        "🍒🍒❓  |  🍋❓🍋  |  ⭐❓⭐"
    )
    winregels_tabel.add_row(
        "Geen prijs (inzet kwijt)",
        "🍒🍋⭐"
    )

    console.print(winregels_tabel)
    while True:
        balance = play_fruitmachine(balance)
        if balance <= 0:
            console.print("Je saldo is op.")
            break
        opnieuw = input("Nog een keer spelen? (ja/nee): ")
        if opnieuw.lower() == "nee":
            break

    return balance

emojij_symbolen = {
    "kers": "🍒",
    "citroen": "🍋",
    "ster": "⭐",
    "druif": "🍇",
    "watermeloen": "🍉",
    "diamant": "💎",
    "klavertje": "🍀",
    "bel": "🔔"
}

def play_fruitmachine(balance: float):
    console.print(f"Je huidige saldo is €{balance:.2f}")
    inzet = float(input("Wat wil je inzetten? €"))
# inzet valideren
    if inzet <= 0:
        console.print("Inzet moet hoger zijn dan 0.")
        return balance

    if inzet > balance:
        console.print("Onvoldoende saldo!")
        return balance
    oud_saldo = balance  #saldo vóór de inzet bewaren
    balance -= inzet


# rollen draaien
    rol1, rol2, rol3 = determine_rolls()
    rollen_tabel = Table(show_header=False, width=50)
    rollen_tabel.add_row(
        f"{emojij_symbolen[rol1]} {rol1}",
        f"{emojij_symbolen[rol2]} {rol2}",
        f"{emojij_symbolen[rol3]} {rol3}",
    )
    console.print(rollen_tabel)

    payout = determine_payout(rol1, rol2, rol3, inzet)
    if payout > 0:
        balance += payout

        if payout == inzet * 3:
            resultaat = "[bold green]Grote prijs! Je wint 3x je inzet.[/bold green]" #Rich markup
        else:
            resultaat = "[bold yellow]Kleine prijs! Je krijgt je inzet terug.[/bold yellow]" #Rich markup
    else:
        resultaat = "[bold red]Helaas geen prijs. Je verliest je inzet.[/bold red]" #Rich markup

    console.print(
        Panel(
            f"{resultaat}\n\n"
            f"Huidig saldo: €{oud_saldo:.2f}\n"  
            f"Inzet: €{inzet:.2f}\n" 
            f"Resterend saldo: €{balance:.2f}",
            title="[bold yellow]🎰 Resultaat 🎰[/bold yellow]",
            border_style="yellow",
            width=50
        )
    )

    return balance

