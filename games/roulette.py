"""
********************     FUNCTIES IN ROULETTE
spin = (round_number * 7) % 37 gewijzigd spin = random.randint(0, 36)
import random
✅ round_number verwijderd
✅ Rich Table
print= console.print
✅ in-text kleuren
✅ winst/verlies met Rich
✅ ongeldige keuze getest
"""
import random


from rich.console import Console
from rich.table import Table
from rich.panel import Panel
console = Console()


def show_options():
    menu = Table(
        title="🎯 ROULETTE 🎯",
        border_style="cyan",
        show_header=False,
        width=50
    )

    menu.add_row("[red]1. Rood[/red]")
    menu.add_row("[white]2. Zwart[/white]")
    menu.add_row("[cyan]3. Even[/cyan]")
    menu.add_row("[magenta]4. Oneven[/magenta]")
    menu.add_row("[yellow]0. Stop[/yellow]")

    console.print(menu)

def get_stake(balance: float) -> float:
    while True:
        try:
            stake = float(input("Hoeveel wil je inzetten? € "))
        except ValueError:
            console.print("[bold red]Voer een geldig bedrag in.[/bold red]")
            continue
        if stake <= 0:
            console.print("[bold red]De inzet moet groter zijn dan 0.[/bold red]")
        elif stake > balance:
            console.print("[bold red]Je hebt niet genoeg saldo voor deze inzet.[/bold red]")
        else:
            return stake

def has_won(choice, color, odd_even):
    if choice == 1 and color == "rood":
        return True
    elif choice == 2 and color == "zwart":
        return True
    elif choice == 3 and odd_even == "even":
        return True
    elif choice == 4 and odd_even == "oneven":
        return True
    return False

def play_roulette(balance: float):

    while True:
        show_options()
        try:
            choice = int(input("Kies je gok(0 om te stoppen): "))
        except ValueError:
            console.print("[bold red]Voer een geldige nummer in van 0 t/m 4.[/bold red]")
            continue

        if choice == 0:
            break
        if choice < 1 or choice > 4:
            console.print("[bold red]Ongeldige keuze, probeer opnieuw.[/bold red]")
            continue

# Vraag hoeveel de gebruiker wil inzetten en check of dat valide is
        console.print(type(balance))
        stake = get_stake(balance)
# Als de inzet geldig is, haal deze van het saldo af.
        oud_saldo = balance
        balance -= stake
        spin = random.randint(0,36)
# Bepaal de kleur
        if spin == 0:
            color = "groen"
            odd_even = "geen"
        elif spin <= 18:
            if spin % 2 == 0:
                color = "zwart"
                odd_even = "even"
            else:
                color = "rood"
                odd_even = "oneven"
        else:
            if spin % 2 == 0:
                color = "rood"
                odd_even = "even"
            else:
                color = "zwart"
                odd_even = "oneven"
# Bereken of de gebruiker gewonnen of verloren heeft.
        win = has_won(choice, color, odd_even)

        if win:
            balance += stake * 2
            resultaat = f"[bold green]Je wint € {stake:.2f}!!![/bold green]"
        else:
            resultaat = f"[bold red]Je verliest € {stake:.2f}[/bold red]"
        console.print(
            Panel(
                f"[bold yellow]De bal valt op {color}{spin}).[/bold yellow]\n\n"
                f"{resultaat}\n\n"
                f"Huidig saldo: €{oud_saldo:.2f}\n"
                f"Inzet: €{stake:.2f}\n"
                f"Resterend saldo: €{balance:.2f}",
                title="[bold cyan]🎯 Roulette resultaat 🎯[/bold cyan]",
                border_style="yellow",
                width=50
            )

        )
# Print eindsaldo van de gebruiker
    return balance
