from datetime import datetime
MIN_AGE = 18
players = {}
current_player = None


#functie voor bepalen begroeting ( uit main)                                                                   #functie:
def determine_salutation(name, gender):
    if gender == "m":
        return f"meneer {name}"
    elif gender == "v":
        return f"mevrouw {name}"
    else:
        return f"speler {name}"

def get_age(birthdate):
    try:
        birth_date = datetime.strptime(birthdate, "%d-%m-%Y")
        today = datetime.today()  # 🟨 NIEUW

        age = today.year - birth_date.year  # 🟨 AANGEPAST

        if (today.month, today.day) < (birth_date.month, birth_date.day):  # 🟨 NIEUW
            age -= 1  # 🟨 NIEUW

        return age

    except ValueError:
        return None

def check_age(age):
    return age >= MIN_AGE

def create_profile(name, birthdate, gender, balance):
    return {
        "naam": name,
        "geboortedatum": birthdate,
        "gender": gender,
        "saldo": balance,
        "gespeelde_spellen": {}
    }
def create_start_players():
    return {
        "Jane": {
            "naam": "Jane",
            "geboortedatum": "20-04-1971",
            "gender": "v",
            "saldo": 500.00,
            "gespeelde_spellen": {}
        },

        "Frank": {
            "naam": "Frank",
            "geboortedatum": "12-03-1971",
            "gender": "m",
            "saldo": 500.00,
            "gespeelde_spellen": {}
        },

        "Jade": {
            "naam": "Jade",
            "geboortedatum": "15-06-1994",
            "gender": "m",
            "saldo": 500.00,
            "gespeelde_spellen": {},
        }
    }
def initialize_player(total_cost):
    global players
    global current_player

    players = create_start_players()

    name = input("Wat is je naam? ").capitalize()

    current_player = name

    if name in players:

        profile = players[current_player]

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

    startbudget = float(
        input("Hoeveel geld neem je mee? €")
    )

    balance = startbudget - total_cost

    players[name] = create_profile(
        name,
        birthdate,
        gender,
        balance
    )

    current_player = name

    print(f"Account voor {name} aangemaakt.")

def get_current_balance():
    return players[current_player]["saldo"]

def update_current_balance(balance):
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

    for name, profile in players.items():

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

    current_player = name

    print(f"Ingelogd als {name}")

def remove_account():
    global current_player

    name = input(
    "Welk account wil je verwijderen? "
    ).capitalize()

    if name not in players:
        print("Dit account bestaat niet.")
        return

    if len(players) == 1:
        print(
            "Laatste account mag niet verwijderd worden."
    )
        return

    del players[name]

    if name == current_player:
        current_player = list(
        players.keys()
        )[0]

    print("Account verwijderd.")




