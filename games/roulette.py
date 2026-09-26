#_______________________________________________________________________________
# stappenplan, programma verloop:
# laat gebruiker een keuze maken/ kleur kiezen
# laat de gebruiker zijn inzet invoeren
# BONUS: valideer of de gebruiker een geldige invoer heeft gegeven.
# Vraag hoeveel de gebruiker wil inzetten en check of dat valide is
# Als de inzet valide is, haal dit dan van de balance af.
# Bepaal de kleur
# Bereken of de gebruiker gewonnen of verloren heeft.
# Printout of de gebruiker gewonnen of verloren heeft.
# Vergeet niet om het rondenummer op te tellen, anders speel je elke ronde hetzelfde spel.
# Print eindsaldo van de gebruiker

#Funties:
# functie 1: def show_options
# functie 2: def get_stake
# functie 3: def has_won
# functie 4: def play_roulette
#-------------------------------------------------------------------------------

def show_options():                                                                           #functie 1
    print()
    print("Kies één van de volgende opties:")
    print("1. Rood")
    print("2. Zwart")
    print("3. Even")
    print("4. Oneven")
    print("0. Stop")
    print()

def get_stake(balance):                                                                       #functie 2
    while True:
        stake = float(input("Hoeveel wil je inzetten? € "))
        if stake <= 0:
            print("De inzet moet groter zijn dan 0.\n")
        elif stake > balance:
            print("Je hebt niet genoeg saldo voor deze inzet.\n")
        else:
            return stake

def has_won(choice, color, odd_even):                             # functie 3
    if choice == 1 and color == "rood":
        return True
    elif choice == 2 and color == "zwart":
        return True
    elif choice == 3 and odd_even == "even":
        return True
    elif choice == 4 and odd_even == "oneven":
        return True
    return False

def play_roulette(balance):                                                        #functie : 4
    round_number = 1
    while True:
        show_options()
        choice = int(input("Kies je gok (0 om te stoppen): "))
        if choice == 0:
            break
# BONUS: valideer of de gebruiker een geldige invoer heeft gegeven.
        if choice < 1 or choice > 4:
            print("Ongeldige keuze, probeer opnieuw.\n")
            continue
# Vraag hoeveel de gebruiker wil inzetten en check of dat valide is
        stake = get_stake(balance)
# Als de inzet valide is, haal dit dan van de balance af.
        balance -= stake
        spin = (round_number * 7) % 37
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
# Printout of de gebruiker gewonnen of verloren heeft.
# Vergeet niet om het rondenummer op te tellen, anders speel je elke ronde hetzelfde spel.
        print()
        print(f"De bal valt op {color} ({spin}).")
        if win:
            balance += stake * 2
            print(f"Je wint € {stake:.2f}")
        else:
            print(f"Je verliest € {stake:.2f}")
        round_number += 1
# Print eindsaldo van de gebruiker
    return balance
