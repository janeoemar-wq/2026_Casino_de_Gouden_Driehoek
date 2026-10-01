"""
verplaatst  naar profile:
MIN_AGE = 18
def get_age(birthdate):
day, month, year = birthdate.split("-")
age = 2026 - int(year)
return age
initialize_player()

verwijderd:
def show_welcome_message(startbudget, balance, salutation): =

"""

from fruitmachine import play_fruitmachine
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

TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00
MIN_AGE = 18
print()

def main():                                                                                                   #functie:1
    print("**************************     LET'S PLAY     ************************")
    print()

    total_cost = (
            TICKET_PRICE
            + CONSUMPTION_PRICE
            + GAMBLING_TAX
    )

    toegang = initialize_player(total_cost)
    if toegang is False:  # 🟨 NIEUW
        return

    opnieuw_inloggen = show_main_menu()

    if opnieuw_inloggen:
        print("\n🔐 Kies opnieuw een account.")
        initialize_player(total_cost)
                                                                          #functie:2
#functie gemaakt voor welkoms bericht                                                                         #functie:4
def show_welcome_message(startbudget, balance, salutation):
    total = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX
    if balance < 0:
        print("\nOnvoldoende budget om het casino te betreden.")
        print(f"Je komt €{-balance:.2f} tekort.")
        return

    print("\nCasino de Gouden Driehoek")
    print("*" * 27)
    print(f"Welkom, {salutation}")
    print()
    print(f"Startbudget:    € {startbudget:.2f}")
    print(f"Vaste kosten:   € {total:.2f}")
    print(f"Saldo:          € {balance:.2f}")
    print()
#functie gemaakt voor hoofdmenu
def show_main_menu():                                                     #functie:5
    while True:
        print("\n=== Hoofdmenu ===")
        print("1. Spellen")
        print("2. Saldo")
        print("3. Account")
        print("0. Stop")

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
                print("Programma wordt afgesloten...")
                break
            case _:
                print("Ongeldige keuze, probeer opnieuw.")

#functie gemaakt voor games menu
def show_games_menu():
    round_number = 0
    while True:
        print("\n=== Spellen Menu ===")
        print("1. Fruitmachine")
        print("2. Roulette")
        print("3. Blackjack")
        print("0. Terug")

        keuze = input("Maak een keuze uit: ")

        match keuze:
                case "1":
                    balance = get_current_balance()
                    balance = play_fruitmachine(balance, round_number)
                    update_current_balance(balance)
                    register_played_game("fruitmachine")
                    round_number += 1

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
                    print("Ongeldige keuze, probeer opnieuw.")
#functie gemaakt voor saldo
def show_balance(balance):                                                                                   #functie: 7
    print(f"\nJe huidige saldo is: €{balance:.2f}")

def show_account_menu():
    while True:
        show_account()

        print("\n1. Toon alle accounts")
        print("2. Nieuw account")
        print("3. Wissel account")
        print("4. Verwijder account")
        print("0. Terug")

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
                print("Ongeldige keuze, probeer opnieuw.")

main()