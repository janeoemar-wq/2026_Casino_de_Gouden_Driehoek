def show_account_menu():

    while True:

        show_account()

        print("\n1. Toon alle accounts")
        print("2. Nieuw account")
        print("3. Wissel account")
        print("4. Verwijder account")
        print("0. Terug")

        choice = input("Keuze: ")

        match choice:

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
                remove_account()

            case "0":
                break