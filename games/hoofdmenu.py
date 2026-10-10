"""
installatie rich en imports

Console
Panel
in-text markup
🟡 Table toevoegen
🟡 Print() nog omzetten
✅  verrverwijderd
⏳ hoofdmenu naar Rich
⏳ accountmenu naar Rich
🟢 STANDAARD OPMAAK: 🟡 Geel voor titels/ 🔵 Cyan voor informatie
🎰 Fruitmachine: gele rand/🎯 Roulette: cyan rand/ blackjack.... rand/🟢 Winst/succes: groen/🔴 Verlies/fout: rood/
Alle Panel/Table: width=50/ 🟣Magenta kan bijvoorbeeld voor een andere menuoptie:

"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

from fruitmachine import start
from roulette import play_roulette
from blackjack import play_blackjack
from profiles import (
    initialize_player,
    create_account,
    show_account,
    show_all_players,
    switch_account,
    remove_account,
    get_current_balance,
    update_current_balance,
    register_played_game
)
console = Console()

TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00
MIN_AGE = 18
print()

def main():
    print("**********     CASINO DE GOUDEN DRIEHOEK dit moet ik nog opleuken    ************")

    total_cost = (
            TICKET_PRICE
            + CONSUMPTION_PRICE
            + GAMBLING_TAX
    )

    toegang = initialize_player(total_cost)
    if toegang is False:
        return


    while True:
        opnieuw_inloggen = show_main_menu()

        if opnieuw_inloggen:
            console.print("\n[bold yellow]🔐 Kies opnieuw een account.[/bold yellow]")
            toegang = initialize_player(total_cost)
            if toegang is False:
                return
        else:
            break

def show_main_menu():
    while True:
        menu = Table(
            title="[yellow]HOOFDMENU[/yellow]",
            border_style="yellow",
            show_header=False,
            width=50,
            box = box.DOUBLE
        )
        menu.add_row("[blue]1. Spellen[/blue]")
        menu.add_row("[magenta]2. Saldo[/magenta]")
        menu.add_row("[cyan]3. Account[/cyan]")
        menu.add_row("[red]0. Stop[/red]")
        console.print(menu)

        keuze = input("Maak een keuze: ")

        match keuze:
            case "1":
                show_games_menu()
            case "2":
                balance = get_current_balance()
                show_balance(balance)
            case "3":
                uitgelogd = show_account_menu()
                if uitgelogd:
                    return True
            case "0":
                console.print("[bold red]Programma wordt afgesloten...[/bold red]")

                break
            case _:
                console.print("[bold red]Ongeldige keuze, probeer opnieuw.[/bold red]")

# 0 spaties
def show_games_menu():

    while True:
        menu = (
            "[bold][yellow]1. Fruitmachine[/yellow]\n"
            "[cyan]2. Roulette[/cyan]\n"
            "[magenta]3. Blackjack[/magenta]\n"
            "[red]0. Terug[/red]"
        )

        console.print(
            Panel(
                menu,
                title= "[bold yellow]🎰 SPELLEN MENU 🎰[/bold yellow]",
                border_style="yellow",
                width=60
            )
        )


        keuze = input("Maak een keuze uit: ")

        match keuze:
            case "1":
                balance = get_current_balance()
                balance = start(balance)
                update_current_balance(balance)
                register_played_game("fruitmachine")

            case "2":
                balance = get_current_balance()
                balance = play_roulette(balance)
                update_current_balance(balance)
                register_played_game("roulette")

            case "3":
                balance = get_current_balance()
                balance = play_blackjack(balance)
                update_current_balance(balance)
                register_played_game("blackjack")

            case "0":
                return
            case _:
                console.print("[bold red]Ongeldige keuze, probeer opnieuw.[/bold red]")

def show_balance(balance):
    console.print(
        Panel(
            f"\n[bold green]Je huidige 💰 SALDO 💰is: €{balance:.2f}[bold green]",
            title="[bold yellow] saldo [/bold yellow]",
            border_style="green",
            width=50
        )
    )

def show_account_menu():
    while True:
        show_account()
        account_menu =Table(
            title="👤 ACCOUNTMENU 👤",
            border_style="yellow",
            show_header = False,
            width = 50,
            box = box.DOUBLE
        )
        account_menu.add_row("[yellow]1. Toon alle accounts[/yellow]")
        account_menu.add_row("[cyan]2. Nieuw account[/cyan]")
        account_menu.add_row("[magenta]3. Wissel account[/magenta]")
        account_menu.add_row("[green]4. Verwijder account[/green]")
        account_menu.add_row("[red]0. Terug[/red]")
        console.print(account_menu)

        keuze = input("Keuze: ")

        match keuze:
            case "1":
                show_all_players()

            case "2":
                create_account(
                    TICKET_PRICE
                    + CONSUMPTION_PRICE
                    + GAMBLING_TAX
                )

            case "3":
                switch_account()

            case "4":
                uitgelogd = remove_account()
                if uitgelogd:
                    return True

            case "0":
                break
            case _:
                console.print("[bold red]Ongeldige keuze, probeer opnieuw.[/bold red]")

main()