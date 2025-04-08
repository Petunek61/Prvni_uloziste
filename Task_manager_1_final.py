# Seznam pro ukládání úkolů
ukoly = []

# Hlavní menu programu
def hlavni_menu():
    while True:
        print("\nSprávce úkolů – Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

# Funkce pro přidání nového úkolu
def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if nazev:  # Pokud je název platný
            while True:
                popis = input("Zadejte popis úkolu: ").strip()
                if popis:  # Pokud je popis platný
                    # Úkol je kompletní a přidá se do seznamu
                    ukoly.append({"Název": nazev, "Popis": popis})
                    print(f"Úkol '{nazev}' byl úspěšně přidán!")
                    return  # Ukončíme funkci po přidání úkolu
                else:
                    print("Popis úkolu nesmí být prázdný nebo obsahovat jen mezery. Zkuste to znovu.")
        else:
            print("Název úkolu nesmí být prázdný nebo obsahovat jen mezery. Zkuste to znovu.")

# Funkce pro zobrazení úkolů
def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("Seznam úkolů:")
        for idx, ukol in enumerate(ukoly, start=1):
            print(f"{idx}. {ukol['Název']} – {ukol['Popis']}")

# Funkce pro odstranění úkolu
def odstranit_ukol():
    if not ukoly:
        print("Seznam úkolů je prázdný, není co odstraňovat.")
        return

    zobrazit_ukoly()
    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odstraneny_ukol = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstraneny_ukol['Název']}' byl odstraněn.")
        else:
            print("Neplatné číslo úkolu.")
    except ValueError:
        print("Zadejte platné číslo.")

# Spuštění programu
hlavni_menu()