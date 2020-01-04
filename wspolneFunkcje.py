import random


def ponowneRozpoczecie(stanKonta):
    wybor = False
    ponownaGra = str("")
    while not wybor:
        if stanKonta == 0:
            doWidzenia(stanKonta, True)
        ponownaGra = str(
            input("Czy chciałbyś zagrać ponownie? Wpisz 1 jeżeli tak lub 0 jeżeli chcesz wrócić do menu gier "))
        if ponownaGra == "1":
            wybor = True
        elif ponownaGra == "0":
            wybor = True
        else:
            print("Błędne wprowadzenie, wprowadź 1 aby rozpocząć nową grę lub 0 aby wrócić do menu gier")
    return ponownaGra


def rozpoczecie():
    rozp = False
    zj = str("")
    print("Wpisz 1 aby rozpocząć grę, lub 0 aby wyjść z niej")
    while not rozp:
        zj = str(input())
        if zj == "1":
            rozp = True
        elif zj == "0":
            rozp = True
        else:
            print("Błędne wprowadzenie, wprowadź jeszcze raz 1 albo 0")
    return zj


def doWidzenia(stanKonta, bylWKasynie):
    print("Do widzenia! Do zobaczenia następnym razem!")
    if bylWKasynie:
        if stanKonta == 0:
            print("Twoj stan konta wynosi 0 więc wypadasz z kasyna!")
        else:
            print("Twoj stan konta po wyjsciu wynosi " + str(stanKonta))
    quit()


def dobieranieKarty(karty, kartyUczestnika):
    czyDobrana = False
    while not czyDobrana:
        nazwa, slownikWartosci = random.choice(list(karty.items()))
        wartosc, czyWybrana = random.choice(list(slownikWartosci.items()))
        if not czyWybrana:
            kartyUczestnika.append([nazwa, wartosc])
            karty[nazwa][wartosc] = True
            czyDobrana = True
    return kartyUczestnika
