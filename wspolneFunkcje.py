import random


def doWidzenia(stanKonta, bylWKasynie):
    print("Do widzenia! Do zobaczenia następnym razem!")
    if bylWKasynie == True:
        if stanKonta == 0:
            print("Twoj stan konta wynosi 0 więc wypadasz z kasyna!")
        else:
            print("Twoj stan konta po wyjsciu wynosi " + str(stanKonta))
    quit()


def kwotaDoObstawienia(stanKonta):
    kwotaWprowadzona = False
    while kwotaWprowadzona == False:
        kwota= int(input("Wprowadz kwotę jaką chcesz obstawić. Dostępny jest przedział od 0 do " + str(stanKonta) + " " ))
        if kwota <= 0:
            print("Nie można wprowadzić ujemnej ani zerowej kwoty, wprowadź jeszcze raz")
        elif kwota > stanKonta:
            print("Nie masz tyle pieniedzy, sprobuj jeszcze raz")
        else:
            kwotaWprowadzona = True
    return kwota


def dobieranieKarty(karty, kartyUczestnika):
    czyDobrana = False
    while czyDobrana == False:
        nazwa, slownikWartosci = random.choice(list(karty.items()))
        wartosc, czyWybrana = random.choice(list(slownikWartosci.items()))
        if czyWybrana == False:
            kartyUczestnika.append([nazwa, wartosc])
            karty[nazwa][wartosc] = True
            czyDobrana = True
    return kartyUczestnika