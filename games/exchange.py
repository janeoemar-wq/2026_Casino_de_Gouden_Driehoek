#week 7 opdracht
import requests
import os # is om mijn API key uit mijn .env te halen
from dotenv import load_dotenv # is nodig om het .env-bestand in te lezen

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
load_dotenv() # Leest de gegevens uit het .env-bestand in.
console = Console() # Maakt een Rich Console-object aan voor opgemaakte uitvoer.
MIJN_API_KEY = os.getenv("EXCHANGE_API_KEY") # Haalt de API-key uit het .env-bestand op.
if not MIJN_API_KEY: # Controleert of de API-key bestaat.
    console.print(
        "[red]Geen API-key gevonden in .env[/red]"
    )
    quit()

#hulpfunctie 1: hier haalt de api met mijn API-Key de ondersteunde valuta,
def toon_valuta(data, start):
    table = Table(
        border_style="bright_yellow",
        show_header=False
    )

    codes = []

    for code, naam in data["supported_codes"]:
        codes.append(f"{code} - {naam}")

    pagina = codes[start:start + 30]

    for a in range(10):
        kolom1 = pagina[a] if a < len(pagina) else ""
        kolom2 = pagina[a + 10] if a + 10 < len(pagina) else ""
        kolom3 = pagina[a + 20] if a + 20 < len(pagina) else ""

        table.add_row(kolom1, kolom2, kolom3)

    console.print(
        Panel(
            table,
            title="Ondersteunde valuta: Code | Land | Munteenheid",
            border_style="bright_yellow",
            width=120
        )
    )

#Hulpfunctie 32
def haal_geldige_valuta_op():
    url = f"https://v6.exchangerate-api.com/v6/{MIJN_API_KEY}/codes"
    #Antwoord van mijn request is, vertaald in jason taal:
    response = requests.get(url)
    data = response.json()

    # afhandelern foutieve API-respons
    if "supported_codes" not in data:
        console.print(
            "[red]Geen valutalijst ontvangen.[/red]"
        )
        return [], {}

    # ik wil alle valutanamen die ik van json krijg in een table met 3 kolommen
    toon_valuta(data, 0)

#STAP 2 lijst met gedlige valuta
    geldige_valuta = []

    for code, naam in data["supported_codes"]:
        geldige_valuta.append(code)
    return geldige_valuta, data

# gebruikersinvoerfunctie:
def get_exchange_request():
    geldige_valuta, data = haal_geldige_valuta_op()

    start = 0

    van_bron_valuta = input(
        "VAN welk munteenheid wil je de geld omzetten?\n"
        "Voer een 3-letterige valutacode in of typ 'MEER': "
    ).strip().upper()

    if van_bron_valuta == "STOP":
        return None, None

    console.print()
    while van_bron_valuta not in geldige_valuta:
        if van_bron_valuta == "MEER":
            start += 30
            toon_valuta(data, start)
        else:
            console.print("Ongeldige invoer!", style="red")

        van_bron_valuta = input(
            "Voer een 3-letterige valutacode in of typ 'MEER': "
        ).strip().upper()

    while True:
        try:
            bedrag = float(
                input(
                    f"Hoeveel {van_bron_valuta} wil je omrekenen? "
                )
            )

            break

        except ValueError:
            console.print(
                "[red]Voer een geldig bedrag in.[/red]"
            )

    return van_bron_valuta, bedrag

#wisselkoers ophalen
def get_exchange_rate_for_currency(currency):
    url = (
        f"https://v6.exchangerate-api.com/v6/"
        f"{MIJN_API_KEY}/latest/{currency}"
    )
    try:
        response = requests.get(url)
#ConnectionError afhandelen
    except requests.exceptions.ConnectionError:
        console.print(
            "[red]De wisselkoers API is niet bereikbaar.[/red]"
        )
#None teruggeven bij fout
        return None
#statuscode controleren
    if response.status_code != 200:
        console.print(
            "[red]Fout bij ophalen van wisselkoers.[/red]"
        )
        return None

    data = response.json()

    return data["conversion_rates"]["EUR"]

# berekening
def convert_to_euro(
    foreign_currency_amount,
    exchange_rate
):
    return (
            foreign_currency_amount
            * exchange_rate
    )

#Output
def print_exchange_result(
    foreign_currency_amount,
    currency,
    exchange_rate,
    euro_amount
):
    console.print(
        Panel(
            (
                f"Bedrag: "
                f"{foreign_currency_amount:.2f} {currency}\n"
                f"Koers naar euro: "
                f"{exchange_rate:.4f}\n"
                f"Euro's: "
                f"€ {euro_amount:.2f}"
            ),
            title="Valuta Converter",
            border_style="bright_yellow",
            width=50
        )
    )

#orkestratie functie/ hoofdfunctie/ WISSELKANTOOR HOOFDMENU
def run_exchange():

    currency, foreign_currency_amount = (
        get_exchange_request()
    )

    if (
            currency is None
            or foreign_currency_amount is None
    ):
        return None

    exchange_rate = (
        get_exchange_rate_for_currency(
            currency
        )
    )

    if exchange_rate is None:
        return None

    euro_amount = convert_to_euro(
        foreign_currency_amount,
        exchange_rate
    )

    print_exchange_result(
        foreign_currency_amount,
        currency,
        exchange_rate,
        euro_amount
    )

    return euro_amount

def toon_valuta(data, start):
    table = Table(
        border_style="bright_yellow",
        show_header=False
    )

    codes = []

    for code, naam in data["supported_codes"]:
        codes.append(f"{code} - {naam}")

    pagina = codes[start:start + 30]

    for a in range(10):
        kolom1 = pagina[a] if a < len(pagina) else ""
        kolom2 = pagina[a + 10] if a + 10 < len(pagina) else ""
        kolom3 = pagina[a + 20] if a + 20 < len(pagina) else ""

        table.add_row(kolom1, kolom2, kolom3)

    console.print(
        Panel(
            table,
            title="Ondersteunde valuta: Code | Land | Munteenheid",
            border_style="bright_yellow",
            width=120
        )
    )
#Hulpfunctie 32
def haal_geldige_valuta_op():
    url = f"https://v6.exchangerate-api.com/v6/{MIJN_API_KEY}/codes"
    #Antwoord van mijn request is, vertaald in jason taal:
    response = requests.get(url)
    data = response.json()

    # afhandelern foutieve API-respons
    if "supported_codes" not in data:
        console.print(
            "[red]Geen valutalijst ontvangen.[/red]"
        )
        return [], {}

    # ik wil alle valutanamen die ik van json krijg in een table met 3 kolommen
    toon_valuta(data, 0)

#STAP 2 lijst met gedlige valuta
    geldige_valuta = []

    for code, naam in data["supported_codes"]:
        geldige_valuta.append(code)
    return geldige_valuta, data


# gebruikersinvoerfunctie:
def get_exchange_request():
    geldige_valuta, data = haal_geldige_valuta_op()

    start = 0

    van_bron_valuta = input(
        "VAN welk munteenheid wil je de geld omzetten?\n"
        "Voer een 3-letterige valutacode in of typ 'MEER': "
    ).strip().upper()

    if van_bron_valuta == "STOP":
        return None, None

    console.print()
    while van_bron_valuta not in geldige_valuta:
        if van_bron_valuta == "MEER":
            start += 30
            toon_valuta(data, start)
        else:
            console.print("Ongeldige invoer!", style="red")

        van_bron_valuta = input(
            "Voer een 3-letterige valutacode in of typ 'MEER': "
        ).strip().upper()

    while True:
        try:
            bedrag = float(
                input(
                    f"Hoeveel {van_bron_valuta} wil je omrekenen? "
                )
            )

            break

        except ValueError:
            console.print(
                "[red]Voer een geldig bedrag in.[/red]"
            )

    return van_bron_valuta, bedrag
#wisselkoers ophalen
def get_exchange_rate_for_currency(currency):
    url = (
        f"https://v6.exchangerate-api.com/v6/"
        f"{MIJN_API_KEY}/latest/{currency}"
    )
    try:
        response = requests.get(url)
#ConnectionError afhandelen
    except requests.exceptions.ConnectionError:
        console.print(
            "[red]De wisselkoers API is niet bereikbaar.[/red]"
        )
#None teruggeven bij fout
        return None
#statuscode controleren
    if response.status_code != 200:
        console.print(
            "[red]Fout bij ophalen van wisselkoers.[/red]"
        )
        return None

    data = response.json()

    return data["conversion_rates"]["EUR"]

# berekening
def convert_to_euro(
    foreign_currency_amount,
    exchange_rate
):
    return (
            foreign_currency_amount
            * exchange_rate
    )


#Output
def print_exchange_result(
    foreign_currency_amount,
    currency,
    exchange_rate,
    euro_amount
):
    console.print(
        Panel(
            (
                f"Bedrag: "
                f"{foreign_currency_amount:.2f} {currency}\n"
                f"Koers naar euro: "
                f"{exchange_rate:.4f}\n"
                f"Euro's: "
                f"€ {euro_amount:.2f}"
            ),
            title="Valuta Converter",
            border_style="bright_yellow",
            width=50
        )
    )

#orkestratie functie/ hoofdfunctie/ WISSELKANTOOR HOOFDMENU
def run_exchange():


    currency, foreign_currency_amount = (
        get_exchange_request()
    )

    if (
            currency is None
            or foreign_currency_amount is None
    ):
        return None

    exchange_rate = (
        get_exchange_rate_for_currency(
            currency
        )
    )

    if exchange_rate is None:
        return None

    euro_amount = convert_to_euro(
        foreign_currency_amount,
        exchange_rate
    )

    print_exchange_result(
        foreign_currency_amount,
        currency,
        exchange_rate,
        euro_amount
    )

    return euro_amount


