import random
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
    if (graczMaAsa == True and punktyGracza + 10<=21):
        punktyGracza +=10
    for i in range(len(kartyDealera)):
        wartosc = kartyDealera[i][1]
        punktyKarty = punkty(wartosc)
        if wartosc == 'As':
            dealerMaAsa = True
        punktyDealera += punktyKarty
    return punktyGracza, punktyDealera
    
        

def rundaBlackjack(karty):
    kartyGracza = []
    kartyDealera = []
    while len(kartyGracza) < 2:
        nazwa, slownikWartosci = random.choice(list(karty.items()))
        wartosc, czyWybrana = random.choice(list(slownikWartosci.items()))
        if czyWybrana == False:
            kartyGracza.append([nazwa,wartosc])
            karty[nazwa][wartosc] = True
    while len(kartyDealera) < 2:
        nazwa, slownikWartosci = random.choice(list(karty.items()))
        wartosc, czyWybrana = random.choice(list(slownikWartosci.items()))
        if czyWybrana == False:
            kartyDealera.append([nazwa,wartosc])
            karty[nazwa][wartosc] = True
    punktacjaGracza, punktacjaDealera  = punktacjaKart(kartyGracza,kartyDealera)
    print("Karty dealera to:")
    for i in range(len(kartyDealera)):
        print(kartyDealera[i][1] + " " + kartyDealera[i][0])
    print("(Punktacja kart: " + str(punktacjaDealera) + ")")
    print(" ")
    print("Karty gracza to:")
    for i in range(len(kartyGracza)):
        print(kartyGracza[i][1] + " " + kartyGracza[i][0])
    print("(Punktacja kart: " + str(punktacjaGracza) + ")")


def blackjackWprowadzenie():
    karty = {'Serce': {'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False, 'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False, 'Król': False, 'As': False}, 'Piki':{'Dwa': False, 'Trzy': False, 'Cztery': False, 'Piec': False, 'Szesc': False, 'Siedem': False, 'Osiem': False, 'Dziewiec': False, 'Dziesiec': False, 'Walet': False, 'Dama': False, 'Król': False, 'As': False}, 'Trefle':{'Dwa': False, 'Trzy': False, 'Cztery': False, 'Piec': False, 'Szesc': False, 'Siedem': False, 'Osiem': False, 'Dziewiec': False, 'Dziesiec': False, 'Walet': False, 'Dama': False, 'Król': False, 'As': False},'Kiery':{'Dwa': False, 'Trzy': False, 'Cztery': False, 'Piec': False, 'Szesc': False, 'Siedem': False, 'Osiem': False, 'Dziewiec': False, 'Dziesiec': False, 'Walet': False, 'Dama': False, 'Król': False, 'As': False}}
    print("Wpisz 1 aby rozpocząć grę, lub 0 aby wyjść z niej")
    rozpoczecie = False
    while rozpoczecie == False:
        zeroJeden = int(input())
        if zeroJeden == 1:
            rozpoczecie = True
        elif zeroJeden == 0:
            rozpoczecie = True
        else:
            print("Błędne wprowadzenie, wprowadź jeszcze raz 1 albo 0")
    if zeroJeden == 1:
        rundaBlackjack(karty)
    else:
        menuGier()

def menuGier():
    czyWKasynie = True
    print("Menu Gier")
    print("Twoj aktualny stan konta to " + str(stanKonta) + ". W co chciałbyś aktualnie zagrać?")
    listaGier = ['blackjack','bcd','cde','def','efg']
    for i in range(len(listaGier)):
        print("Jeżeli chcesz zagrać w " + listaGier[i] + " wybierz " + str(i+1))
    print("Jeżeli chcesz wyjść z kasyna wybierz 0")
    prawidlowyWybor = False
    while prawidlowyWybor == False:
        wybor = int(input())
        if wybor == 1:
            print("Witamy w grze blackjack")
            blackjackWprowadzenie()
            prawidlowyWybor = True
        elif wybor == 2:
            print("2")
            prawidlowyWybor = True
        elif wybor == 3:
            print("3")
            prawidlowyWybor = True
        elif wybor == 4:
             print("4")
             prawidlowyWybor = True
        elif wybor == 5:
            print("5")
            prawidlowyWybor = True
        elif wybor == 0:
            doWidzenia(czyWKasynie)
            prawidlowyWybor = True
        else:
            print("Bledny wybor sprobuj ponownie ")

def doWidzenia(bylWKasynie):
    print("Do widzenia! Do zobaczenia następnym razem!")
    if bylWKasynie == True:
        print("Twoj stan konta po wyjsciu wynosi " + str(stanKonta))
    quit()

def czyChceszWejsc():
    tak = False
    while tak == False:
        wejscie = str(input("Czy jestes pewien, ze chcesz rzucic sie w wir szaleństwa kasynowego? [T/N] "))
        if wejscie == "T":
            print("Super! Zaczynajmy!")
            tak = True
        elif wejscie == "N":
            print("Szkoda!")
            doWidzenia(czyWKasynie)
            break
        else:
            blad()
    if tak == True:
        menuGier()
        
def blad():
    print("Błąd wprowadzenia, powtórz, wpisując T dla tak lub N dla nie")

def czyPelnoletni():
    pelnoletni = False
    while pelnoletni == False:
        pelnoletnosc = str(input("Czy jesteś pełnoletni? [T/N] " ))
        if pelnoletnosc == "T":
            print("Super, czyli możesz wejść do kasyna!")
            pelnoletni = True
        elif pelnoletnosc == "N":
            print("Niestety musisz opuścić ten lokal")
            doWidzenia(czyWKasynie)
            break
        else:
            blad()
    if pelnoletni == True:
        czyChceszWejsc()

print("Witaj w kasynie W&W")
stanKonta = float(1000)
czyWKasynie = False
czyPelnoletni()
