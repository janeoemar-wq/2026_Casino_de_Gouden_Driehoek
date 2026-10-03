"""
*************************m     FUNCTIES IN FRUITMACHINE
def determine_rolls(round_number)
def determine_payout(rol1, rol2, rol3, inzet)
def start(balance)
def play_fruitmachine(balance, round_number)
"""

def determine_rolls(round_number):
    optie = round_number % 5

    if optie == 0:
        return "kers", "citroen", "ster"
    elif optie == 1:
        return "kers", "kers", "kers"
    elif optie == 2:
        return "ster", "ster", "citroen"
    elif optie == 3:
        return "citroen", "kers", "ster"
    else:
        return "ster", "ster", "ster"

def determine_payout(rol1, rol2, rol3, inzet):
    if rol1 == rol2 == rol3:
        return inzet * 3
    elif rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return inzet
    else:
        return 0

def start(balance):
    print("=== Winregels Fruitmachine ===")
    print("→ Grote prijs (3x inzet) 🍒🍒🍒  | 🍋🍋🍋  | ⭐⭐⭐")
    print("→ Kleine prijs (inzet terug) 🍒🍒❓  | 🍋❓🍋  | ⭐❓⭐")
    print("→ Geen prijs (inzet kwijt) 🍒🍋⭐")
    print("==============================")
    round_number = 0
    while True:
        balance = play_fruitmachine(balance, round_number)
        round_number += 1
        if balance <= 0:
            print("Je saldo is op.")
            break
        opnieuw = input("Nog een keer spelen? (ja/nee): ")
        if opnieuw.lower() == "nee":
            break

    return balance

emojij_lijst = {
    "kers": "🍒",
    "citroen": "🍋",
    "ster": "⭐"}

def play_fruitmachine(balance: float, round_number):
    print(f"Je huidige saldo is €{balance:.2f}")
    inzet = float(input("Wat wil je inzetten? €"))
# inzet valideren
    if inzet <= 0:
        print("Inzet moet hoger zijn dan 0.")
        return balance

    if inzet > balance:
        print("Onvoldoende saldo!")
        return balance
    balance -= inzet

# rollen draaien
    rol1, rol2, rol3 = determine_rolls(round_number)
    print(f"\n | {emojij_lijst[rol1]}  {rol1}| {emojij_lijst[rol2]} {rol2} | {emojij_lijst[rol3]} {rol3}|")

    payout = determine_payout(rol1, rol2, rol3, inzet)
    if payout > 0:
        balance += payout

        if payout == inzet * 3:
            print("\nGrote prijs! Je wint 3x je inzet.")
        else:
            print("\nKleine prijs! Je krijgt je inzet terug.")
    else:
        print("\nHelaas geen prijs. Je verliest je inzet.")

    print(f"Nieuwe balance: €{balance}")
    return balance

