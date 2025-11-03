# Správce úkolu - Hlavní menu

spravceukolu = {}  # slovník: název -> popis

def pridat_ukol():
    nazev = input("Zadej název úkolu: ")
    popis = input("Zadej popis úkolu: ")
    spravceukolu[nazev] = popis
    print(f" Úkol '{nazev}' byl přidán.\n")

def zobrazit_ukoly():
    if not spravceukolu:
        print(" Seznam úkolů je prázdný.\n")
    else:
        print("\n--- Seznam úkolů ---")
        for nazev, popis in spravceukolu.items():
            print(f"- {nazev}: {popis}")
        print("--------------------\n")

def odstranit_ukol():
    nazev = input("Zadej název úkolu, který chceš smazat: ")
    if nazev in spravceukolu:
        spravceukolu.pop(nazev)
        print(f" Úkol '{nazev}' byl smazán.\n")
    else:
        print(f" Úkol '{nazev}' neexistuje.\n")

# Hlavní smyčka programu
while True:
    print("Spravce ukolu Hlavni Menu")
    print("1 - Přidat úkol")
    print("2 - Zobrazit úkoly")
    print("3 - Odstranit úkol")
    print("4 - Konec")

    volba = input("Vyber možnost: ")

    if volba == "1":
        pridat_ukol()
    elif volba == "2":
        zobrazit_ukoly()
    elif volba == "3":
        odstranit_ukol()
    elif volba == "4":
        print(" Ukončuji program. Měj se!")
        break
    else:
        print(" Neplatná volba, zkus to znovu.\n")
