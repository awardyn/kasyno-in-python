import wspolneFunkcje


def punkty(wartosc):
    punktyZdobyte = int(0)
    if wartosc == 'Dwa':
        punktyZdobyte = 2
    elif wartosc == 'Trzy':
        punktyZdobyte = 3
    elif wartosc == 'Cztery':
        punktyZdobyte = 4
    elif wartosc == 'Pięć':
        punktyZdobyte = 5
    elif wartosc == 'Sześć':
        punktyZdobyte = 6
    elif wartosc == 'Siedem':
        punktyZdobyte = 7
    elif wartosc == 'Osiem':
        punktyZdobyte = 8
    elif wartosc == 'Dziewięć':
        punktyZdobyte = 9
    elif wartosc == "Dziesięć":
        punktyZdobyte = 10
    elif wartosc == 'Walet':
        punktyZdobyte = 10
    elif wartosc == 'Dama':
        punktyZdobyte = 10
    elif wartosc == 'Król':
        punktyZdobyte = 10
    elif wartosc == 'As':
        punktyZdobyte = 1
    return punktyZdobyte


def punktacjaKart(kartyGracza, kartyDealera):
    punktyGracza = int(0)
    punktyDealera = int(0)
    graczMaAsa = False
    dealerMaAsa = False
    for i in range(len(kartyGracza)):
        wartosc = kartyGracza[i][1]
        punktyKarty = punkty(wartosc)
        if wartosc == 'As':
            graczMaAsa = True
        punktyGracza += punktyKarty
    if graczMaAsa is True and punktyGracza + 10 <= 21:
        punktyGracza += 10
    for i in range(len(kartyDealera)):
        wartosc = kartyDealera[i][1]
        punktyKarty = punkty(wartosc)
        if wartosc == 'As':
            dealerMaAsa = True
        punktyDealera += punktyKarty
    if dealerMaAsa is True and punktyDealera + 10 <= 21:
        punktyDealera += 10
    return punktyGracza, punktyDealera


def poskonczeniudodawania(punktacjaGracza, punktacjaDealera, karty, kartyDealera, kartyGracza, stanKonta, kwota, ktosWygral):
    while punktacjaDealera <= punktacjaGracza and punktacjaDealera < 21:
        kartyDealera = wspolneFunkcje.dobieranieKarty(karty, kartyDealera)
        punktacjaGracza, punktacjaDealera = punktacjaKart(kartyGracza, kartyDealera)
    if punktacjaGracza < punktacjaDealera <= 21:
        print("Karty dealera to:")
        for i in range(len(kartyDealera)):
            print(kartyDealera[i][1] + " " + kartyDealera[i][0])
        print("(Punktacja kart: " + str(punktacjaDealera) + ")")
        print(" ")
        print("Karty gracza to:")
        for i in range(len(kartyGracza)):
            print(kartyGracza[i][1] + " " + kartyGracza[i][0])
        print("(Punktacja kart: " + str(punktacjaGracza) + ")")
        stanKonta -= kwota
        print("DEALER MA WIĘCEJ PUNKTÓW NIŻ TY I MNIEJ NIŻ 22, PRZEGRAŁEŚ " + str(kwota) + "!")
        ktosWygral = True
    return punktacjaGracza, punktacjaDealera, karty, kartyDealera, kartyGracza, stanKonta, ktosWygral


def wypisanieKart(kartyDealera, kartyGracza, punktacjaGracza, punktacjaDealera):
    print("Karty dealera to:")
    for i in range(len(kartyDealera)):
        print(kartyDealera[i][1] + " " + kartyDealera[i][0])
    print("(Punktacja kart: " + str(punktacjaDealera) + ")")
    print(" ")
    print("Karty gracza to:")
    for i in range(len(kartyGracza)):
        print(kartyGracza[i][1] + " " + kartyGracza[i][0])
    print("(Punktacja kart: " + str(punktacjaGracza) + ")")