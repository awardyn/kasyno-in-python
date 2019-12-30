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
    if graczMaAsa == True and punktyGracza + 10 <= 21:
        punktyGracza += 10
    for i in range(len(kartyDealera)):
        wartosc = kartyDealera[i][1]
        punktyKarty = punkty(wartosc)
        if wartosc == 'As':
            dealerMaAsa = True
        punktyDealera += punktyKarty
    if dealerMaAsa == True and punktyDealera + 10 <= 21:
        punktyDealera += 10
    return punktyGracza, punktyDealera
