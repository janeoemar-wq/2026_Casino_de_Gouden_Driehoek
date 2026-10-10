
"""FUNCTIES IN PROFILES week 6
from datetime import datetime, timedelta vervangen door from datetime import datetime, timedelta, date
"""
from datetime import datetime, timedelta, date
MIN_AGE = 18
players = {}
current_player = None

def determine_salutation(name, gender):
    if gender == "m":
        return f"meneer {name}"
    elif gender == "v":
        return f"mevrouw {name}"
    else:
        return f"speler {name}"

def get_age(birthdate):
    try:
        birthdate_value = datetime.strptime(
            birthdate,
            "%d-%m-%Y"
        ).date()
        today_value = date.today()

        age = today_value.year - birthdate_value.year
        if birthdate_value > today_value:
            raise ValueError("Geboortedatum mag niet in de toekomst liggen.")
        if (
            today_value.month,
            today_value.day
        ) < (
            birthdate_value.month,
            birthdate_value.day
        ):
            age -= 1

        return age

    except ValueError:
        return None

def check_age(age):
    return age >= MIN_AGE

def create_profile(name, birthdate, gender, balance, password):
    return {
        "naam": name,
        "geboortedatum": birthdate,
        "gender": gender,
        "saldo": balance,
        "gespeelde_spellen": {},
        "wachtwoord": password,
        "geblokkeerd tot": None
    }
def create_start_players():
    return {
        "Jane": {
            "naam": "J",
            "geboortedatum": "20-04-1971",
            "gender": "v",
            "saldo": 500.00,
            "gespeelde_spellen": {},
            "wachtwoord": "123",
            "geblokkeerd_tot": None
        },

        "Frank": {
            "naam": "Frank",
            "geboortedatum": "12-03-1971",
            "gender": "m",
            "saldo": 500.00,
            "gespeelde_spellen": {},
            "wachtwoord": "frank123",
            "geblokkeerd_tot": None
        },

        "Jade": {
            "naam": "Jade",
            "geboortedatum": "15-06-1994",
            "gender": "m",
            "saldo": 500.00,
            "gespeelde_spellen": {},
            "wachtwoord": "jade123",
            "geblokkeerd_tot": None
        }
    }
def initialize_player(total_cost):
    global players
    global current_player

    if not players:
        players = create_start_players()

    name = input("Wat is je naam? ").capitalize()

    current_player = name

    if name in players:

        profile = players[current_player]
        if profile["geblokkeerd_tot"] is not None:
            if datetime.now() < profile["geblokkeerd_tot"]:
                print("🔒 Dit account is tijdelijk geblokkeerd.")
                return False

        profile["geblokkeerd_tot":] = None
# stond niet in de opdracht, maar vond het wel leuk om te doen
        for poging in range(3):
            password = input("Voer je wachtwoord in: ")

            if password == profile["wachtwoord"]:
                break

            resterend = 2 - poging
            print("❌ Onjuist wachtwoord.")

            if resterend > 0:
                print(f"Je hebt nog {resterend} poging(en).")

        else:
            profile["geblokkeerd_tot"] = datetime.now() + timedelta(hours=1)
            print("🔒 Te veel foute pogingen. Account is 1 uur geblokkeerd.")
            return False

        salutation = determine_salutation(
            current_player,
            profile["gender"]
        )
        balance = profile["saldo"]

        print("\nWelkom terug!")
        print(f"Welkom {salutation}")
        print(f"Huidig saldo: €{balance:.2f}")
        return True

    else:
        create_account(total_cost, name)
        if name not in players:
            return False
        profile = players[current_player]
        balance = profile["saldo"]
        start_balance = balance + total_cost

        salutation = determine_salutation(
            current_player,
            profile["gender"]
        )

        print("\nCasino de Gouden Driehoek")
        print("*" * 27)
        print(f"Welkom, {salutation}")
        print()
        print(f"Startbudget: € {start_balance:.2f}")
        print(f"Vaste kosten: € {total_cost:.2f}")
        print(f"Saldo: € {balance:.2f}")
        if balance <0:
            print("⛔ Onvoldoende budget om het casino te betreden.")
            print(f"Je komt €{-balance:.2f} tekort.")
            return False
        else:
            print("Je hebt voldoende budget om het casino te betreden.")
            return True

def create_account(total_cost, name=None):
    global players
    global current_player

    if name is None:
        name = input(
            "Naam voor nieuw account: "
        ).capitalize()

        if name in players:
            print("Dit account bestaat al.")
            return
    birthdate = input(
        "Wat is je geboortedatum? "
    )

    age = get_age(birthdate)
    if age is None:
        print("❌ Ongeldige geboortedatum. Gebruik dd-mm-jjjj.")
        return

    if not check_age(age):
        print("⛔  🔞  Je moet 18 jaar of ouder zijn. 🔞  ⛔")
        return
    gender = input(
        "Wat is je gender? (m/v/x) "
    ).lower()
    password = input("Kies een wachtwoord: ")

    startbudget = float(
        input("Hoeveel geld neem je mee? €")
    )

    balance = startbudget - total_cost

    players[name] = create_profile(
        name,
        birthdate,
        gender,
        balance,
        password
    )

    current_player = name

    print(f"Account voor {name} aangemaakt.")

def get_current_balance():# HELPERFUNCTIE
    return players[current_player]["saldo"]

def update_current_balance(balance):# HELPERFUNCTIE
    players[current_player]["saldo"] = balance

def register_played_game(game_name):
    played_games = players[current_player][
"gespeelde_spellen"
]

    if game_name in played_games:
        played_games[game_name] += 1
    else:
        played_games[game_name] = 1

def show_account():

    profile = players[current_player]

    print("\nCasino de Gouden Driehoek")
    print("-------------------------")

    print(f"Speler: {profile['naam']}")
    print(f"Saldo: €{profile['saldo']:.2f}")

    print("\nGespeelde spellen:")

    if profile["gespeelde_spellen"]:

        for game, amount in profile[
        "gespeelde_spellen"
        ].items():

            print(
                f"- {game}: {amount} keer"
    )

    else:
        print("Nog geen spellen gespeeld")

    print("\nBeschikbare spelers:")
    print(list(players.keys()))

def show_all_players():

    print("\nAlle spelers")

    for name, profile in players.items(): #verwijst naar de sleutel-waardeparen van de dictionary players

        print(
            f"- {name}: €{profile['saldo']:.2f}"
)
def switch_account():
    global current_player

    name = input(
    "Naar welk account wil je wisselen? "
    ).capitalize()

    if name not in players:
        print("❌ Dit account bestaat niet.")
        return
    profile = players[name]

    password = input("Voer het wachtwoord van dit account in: ")

    if password != profile["wachtwoord"]:
        print("❌ Onjuist wachtwoord. Account niet gewisseld.")
        return

    current_player = name

    print(f"Ingelogd als {name}")


def remove_account():
    global current_player

    name = input(
    "Welk account wil je verwijderen? "
    ).capitalize()

    if name not in players:
        print("Dit account bestaat niet.")
        return False

    if len(players) == 1:
        print(
            "Laatste account mag niet verwijderd worden."
    )
        return False

    del players[name]

    if name == current_player:
        current_player = None
        print("Account verwijderd.")
        print("🔒 Je bent uitgelogd.")
        return True #de huidige gebruiker is verwijderd, opnieuw inloggen

    print("Account verwijderd.")
    return False #  bv:Als ik Frank verwijder terwijl Jane actief nog is.
    # huidige speler blijft gewoon in het accountmenu.




