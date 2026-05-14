# calorie_prototype.py
# Prototype: berekent calorieen verbrand bij sport
# Formule: Calorieen = MET x gewicht (kg) x duur (uren)
# Auteur: Abdallah Azouagh

# MET-waarden voor verschillende sporten (Metabolic Equivalent of Task)
MET_VALUES = {
    "Wandelen": 3.5,
    "Yoga": 3.0,
    "Krachttraining": 5.0,
    "Zwemmen": 6.0,
    "Tennis": 7.0,
    "Voetbal": 7.0,
    "Fietsen": 8.0,
    "Hardlopen": 10.0,
    "HIIT": 12.0,
}


def bereken_calorieen(gewicht_kg, sport, duur_minuten):
    """Bereken calorieen verbrand + 3 afgeleide outputs."""
    met = MET_VALUES.get(sport, 5.0)
    duur_uren = duur_minuten / 60
    calorieen = met * gewicht_kg * duur_uren

    # Vet-equivalent (1 gram lichaamsvet ~ 9 kcal energie)
    vet_gram = calorieen / 9

    # Voedsel-equivalent (1 chocoladereep ~ 250 kcal)
    chocoladerepen = calorieen / 250

    # Advies op basis van energieverbruik
    if calorieen < 100:
        advies = "Korte sessie. Probeer iets langer voor meer effect!"
    elif calorieen < 300:
        advies = "Goede start! Mooi werk."
    elif calorieen < 600:
        advies = "Indrukwekkende prestatie! Vergeet niet te hydrateren."
    else:
        advies = "Topprestatie! Zorg voor voldoende herstel."

    return calorieen, vet_gram, chocoladerepen, advies


def vraag_positief_getal(prompt):
    """Vraag herhaaldelijk tot een geldig positief getal is ingegeven."""
    while True:
        ruw = input(prompt)
        try:
            waarde = float(ruw)
        except ValueError:
            print("  -> Ongeldige invoer. Geef een numerieke waarde (bv. 75 of 1.80).")
            continue

        if waarde <= 0:
            print("  -> Waarde moet groter zijn dan 0.")
            continue

        return waarde


def vraag_sport_keuze(sport_namen):
    """Vraag herhaaldelijk tot een geldige sport-keuze is ingegeven."""
    while True:
        ruw = input(f"\nKies een sport (nummer 1-{len(sport_namen)}): ")
        try:
            keuze = int(ruw)
        except ValueError:
            print("  -> Ongeldige invoer. Geef een heel getal in.")
            continue

        if not (1 <= keuze <= len(sport_namen)):
            print(f"  -> Kies een nummer tussen 1 en {len(sport_namen)}.")
            continue

        return sport_namen[keuze - 1]


if __name__ == "__main__":
    print("=" * 50)
    print("Calorie-verbruik Calculator - Prototype")
    print("=" * 50)

    # Input 1: lichaamsgewicht
    gewicht = vraag_positief_getal("\nLichaamsgewicht (kg): ")

    # Input 2: sport-keuze (via lijst)
    sport_namen = list(MET_VALUES.keys())
    print("\nBeschikbare sporten:")
    for i, sport in enumerate(sport_namen, 1):
        print(f"  {i}. {sport} (MET: {MET_VALUES[sport]})")

    sport = vraag_sport_keuze(sport_namen)

    # Input 3: duur
    duur = vraag_positief_getal(f"Duur van de {sport}-sessie (minuten): ")

    # Berekening
    cal, vet, repen, advies = bereken_calorieen(gewicht, sport, duur)

    # Output
    print("\n" + "=" * 50)
    print("RESULTAAT")
    print("=" * 50)
    print(f"Calorieen verbrand:       {cal:.1f} kcal")
    print(f"Vet-equivalent:           {vet:.1f} gram")
    print(f"Vergelijking met voedsel: {repen:.2f} chocoladerepen")
    print(f"\nAdvies: {advies}")