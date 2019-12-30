import random


def tworzeniePlanszy():
    mozliweLiczby = []
    for i in range(1, 91):
        mozliweLiczby.append(i)
    planszaBingo90 = []
    for i in range(5):
        wiersz = []
        while len(wiersz) < 5:
            liczba = random.randint(1, 90)
            if liczba in mozliweLiczby:
                wiersz.append(liczba)
                mozliweLiczby.remove(liczba)
        planszaBingo90.append(wiersz)
    return planszaBingo90


def losowanieLiczby(liczby):
    wylosowana = False
    while not wylosowana:
        liczba = random.randint(1, 90)
        if liczba in liczby:
            liczby.remove(liczba)
            wylosowana = True
    return liczba, liczby


def sprawdzenieLiczby(kwota, liczba, stanKonta, planszaGracza, wierszeGracza, kolumnyGracza, wygrana):
    for i in range(len(planszaGracza)):
        for j in range(len(planszaGracza[i])):
            if liczba == planszaGracza[i][j]:
                print("Trafiles liczbe!")
                print(" ")
                if liczba not in wierszeGracza[j]:
                    wierszeGracza[j].append(liczba)
                if liczba not in kolumnyGracza[i]:
                    kolumnyGracza[i].append(liczba)

                if len(wierszeGracza[j]) == 5:
                    print("BINGO! Wygrales " + str(kwota*4))
                    stanKonta = stanKonta + 4 * kwota
                    wygrana = True
                    break
                elif len(kolumnyGracza[i]) == 5:
                    print("BINGO! Wygrales " + str(kwota*4))
                    stanKonta = stanKonta + 4 * kwota
                    wygrana = True
                    break
    return wygrana, stanKonta, wierszeGracza, kolumnyGracza


def sprawdzenieLiczbyKomputer(kwota, liczba, stanKonta, plansza, wiersze, kolumny, nr, wygrana):
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if liczba == plansza[i][j]:
                print("Komputer nr " + str(nr) + " trafil liczbe")
                print(" ")
                if liczba not in wiersze[nr][j]:
                    wiersze[nr][j].append(liczba)
                if liczba not in kolumny[nr][i]:
                    kolumny[nr][i].append(liczba)
                if len(wiersze[nr][j]) == 5:
                    print("BINGO! Komputer nr " + str(nr) + " wygral! Przegrales " + str(kwota))
                    print("Jego plansza wygladala tak: ")
                    print(plansza)
                    stanKonta = stanKonta - kwota
                    wygrana = True
                    break
                elif len(kolumny[nr][i]) == 5:
                    print("BINGO! Komputer nr " + str(nr) + " wygral! Przegrales " + str(kwota))
                    print("Jego plansza wygladala tak: ")
                    print(plansza)
                    stanKonta = stanKonta - kwota
                    wygrana = True
                    break
    return wygrana, stanKonta, wiersze, kolumny
