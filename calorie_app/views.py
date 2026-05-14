# calorie_app/views.py
from django.shortcuts import render

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

    vet_gram = calorieen / 9
    chocoladerepen = calorieen / 250

    if calorieen < 100:
        advies = "Korte sessie. Probeer iets langer voor meer effect!"
    elif calorieen < 300:
        advies = "Goede start! Mooi werk."
    elif calorieen < 600:
        advies = "Indrukwekkende prestatie! Vergeet niet te hydrateren."
    else:
        advies = "Topprestatie! Zorg voor voldoende herstel."

    return calorieen, vet_gram, chocoladerepen, advies


def calorie_form(request):
    """Hoofdview: toont het formulier en het resultaat."""
    context = {
        "sporten": list(MET_VALUES.keys()),
        "resultaat": None,
        "fout": None,
        "form_data": {"gewicht": "", "sport": "", "duur": ""},
    }

    if request.method == "POST":
        # Bewaar ingevulde waarden zodat ze bij fout zichtbaar blijven
        context["form_data"] = {
            "gewicht": request.POST.get("gewicht", ""),
            "sport": request.POST.get("sport", ""),
            "duur": request.POST.get("duur", ""),
        }

        try:
            gewicht = float(request.POST.get("gewicht", "0").replace(",", "."))
            sport = request.POST.get("sport", "")
            duur = float(request.POST.get("duur", "0").replace(",", "."))

            if gewicht <= 0 or duur <= 0:
                raise ValueError("Gewicht en duur moeten groter zijn dan 0.")
            if sport not in MET_VALUES:
                raise ValueError("Ongeldige sport-keuze.")

            cal, vet, repen, advies = bereken_calorieen(gewicht, sport, duur)

            context["resultaat"] = {
                "calorieen": round(cal, 1),
                "vet_gram": round(vet, 1),
                "chocoladerepen": round(repen, 2),
                "advies": advies,
                "gewicht": gewicht,
                "sport": sport,
                "duur": duur,
            }
        except (ValueError, TypeError) as e:
            context["fout"] = f"Ongeldige invoer: {e}"

    return render(request, "calorie_app/form.html", context)