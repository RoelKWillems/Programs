keuze = 0

while keuze != 4:
    print("\n--- Hoofdmenu ---")
    print("1) Server status bekijken")
    print("2) Netwerk scannen")
    print("3) Logs bekijken")
    print("4) Stoppen")

    keuze = int(input("Maak een keuze: "))

    if keuze == 1:
        print("Server status wordt bekeken...")
    elif keuze == 2:
        print("Netwerk wordt gescand...")
    elif keuze == 3:
        print("Logs worden bekeken...")
    elif keuze == 4:
        print("Programma wordt gestopt. Tot ziens!")
    else:
        print("Ongeldige keuze, probeer opnieuw.")