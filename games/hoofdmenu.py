#from games.Archief.testen_oud import test_fruitmachine
from fruitmachine import play_fruitmachine
from roulette import play_roulette
from blackjack import play_blackjack

TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00
MIN_AGE = 18
print()
def main():                                                                                                   #functie:1
    print("**************************    LET'S PLAY    ************************")
    print()
#stap 1a vraag gebuikersgegevens op
    name = input("Wat is je naam? ").capitalize()
    birthdate = input("Wat is je geboortedatum? (dd-mm-yyyy) ")
    gender = input("Wat is je gender? (m/v/x) ").strip().lower()
    startbudget = float(input("Hoeveel geld neem je mee naar Casino de Gouden Driehoek? € "))
#stap 1b bepaal begroeting
    salutation = determine_salutation(name, gender)
#stap 1c controleer leeftijd
    age = get_age(birthdate)
#Als de gebruiker jonger is dan 18, stop het programma met return
    if age < MIN_AGE:
        print(f"\nSorry {salutation}, je moet 18 jaar of ouder zijn om deze applicatie te gebruiken.")
        return
#stap 1d Bereken en controleer de kosten en het saldo
    total_costs = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX
    balance = startbudget - total_costs
#controleer of er genoeg budget is
    if balance < 0:
        print("\nOnvoldoende budget om het casino te betreden.")
        print(f"Je komt €{-balance:.2f} tekort.")
        return
#stap 1e Toon welkomstbericht.
    show_welcome_message(startbudget, balance, salutation)
#stap 1f Start hoofdmenu
    show_main_menu(name, birthdate, salutation, balance)

#functie gemaakt voor leeftijdcheck                                                                           #functie:2
def get_age(birthdate):
    day, month, year = birthdate.split("-")
    age = 2026 - int(year)
    return age

#functie gemaakt voor bepalen begroeting                                                                      #functie:3
def determine_salutation(name, gender):
    if gender == "m":
        return f"meneer {name}"
    elif gender == "v":
        return f"mevrouw {name}"
    else:
        return f"speler {name}"
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
def show_main_menu(name, birthdate, salutation, balance):                                                     #functie:5
    while True:
        print("\n=== Hoofdmenu ===")
        print("1. Spellen")
        print("2. Saldo")
        print("3. Account")
        print("0. Stop")

        keuze = input("Maak een keuze: ")

        match keuze:
            case "1":
                balance = show_games_menu(balance, salutation)
            case "2":
                show_balance(balance)
            case "3":
                show_account(name, birthdate, salutation)
            case "0":
                print("Programma wordt afgesloten...")
                break
            case _:
                print("Ongeldige keuze, probeer opnieuw.")

#functie gemaakt voor games menu
def show_games_menu(balance, salutation):
    round_number = 0
    #functie: 6
    while True:
        print("\n=== Spellen Menu ===")
        print("1. Fruitmachine")
        print("2. Roulette")
        print("3. Blackjack")
        print("0. Terug")

        keuze = input("Maak een keuze uit: ")

        match keuze:
            case "1":
                balance = play_fruitmachine(balance, round_number)
                round_number += 1
            case "2":
                balance = play_roulette(balance)
            case "3":
                balance = play_blackjack(balance)
            case "0":
                return balance
            case _:
                print("Ongeldige keuze, probeer opnieuw.")
#functie gemaakt voor saldo
def show_balance(balance):                                                                                   #functie: 7
    print(f"\nJe huidige saldo is: €{balance:.2f}")
#functie gemaakt voor accountgevens
def show_account(name, birthdate, salutation):                                                               #functie: 8
    print("\n=== Accountgegevens ===")
    print(f"Naam: {salutation}")
    print(f"Geboortedatum: {birthdate}")
main()