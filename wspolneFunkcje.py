import random


def doWidzenia(stanKonta, bylWKasynie):
    print("Do widzenia! Do zobaczenia następnym razem!")
    if bylWKasynie == True:
        if stanKonta == 0:
            print("Twoj stan konta wynosi 0 więc wypadasz z kasyna!")
        else:
            print("Twoj stan konta po wyjsciu wynosi " + str(stanKonta))
    quit()


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