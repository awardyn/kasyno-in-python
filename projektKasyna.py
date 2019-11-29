import random
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
    if (graczMaAsa == True and punktyGracza + 10<=21):
        punktyGracza +=10
    for i in range(len(kartyDealera)):
        wartosc = kartyDealera[i][1]
        punktyKarty = punkty(wartosc)
        if wartosc == 'As':
            dealerMaAsa = True
        punktyDealera += punktyKarty
    if (dealerMaAsa == True and punktyDealera + 10<=21):
        punktyDealera +=10
    return punktyGracza, punktyDealera
    
        

def rundaBlackjack(stanKonta, karty):
    kwotaWprowadzona = False
    while kwotaWprowadzona == False:
        kwota= int(input("Wprowadz kwotę jaką chcesz obstawić. Dostępny jest przedział od 0 do " + str(stanKonta)))
        if kwota<=0:
            print("Nie można wprowadzić ujemnej ani zerowej kwoty, wprowadź jeszcze raz")
        elif kwota>stanKonta:
            print("Nie masz tyle pieniedzy, sprobuj jeszcze raz")
        else:
            kwotaWprowadzona = True
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
    ktosWygral = False
    czySkonczyles = False
    while ktosWygral == False:
        print("Karty dealera to:")
        for i in range(len(kartyDealera)):
            print(kartyDealera[i][1] + " " + kartyDealera[i][0])
        print("(Punktacja kart: " + str(punktacjaDealera) + ")")
        print(" ")
        print("Karty gracza to:")
        for i in range(len(kartyGracza)):
            print(kartyGracza[i][1] + " " + kartyGracza[i][0])
        print("(Punktacja kart: " + str(punktacjaGracza) + ")")

        if punktacjaGracza == 21 and punktacjaDealera == 21:
            print("REMIS")
            ktosWygral = True
        elif punktacjaGracza == 21:
            print("MASZ BLACKJACKA WYGRAŁEŚ!")
            stanKonta +=kwota
            ktosWygral = True
        elif punktacjaDealera == 21:
            stanKonta -=kwota
            print("DEALER MA BLACKJACKA, WYGRAŁ!")
            ktosWygral = True
        elif punktacjaDealera > 21:
            stanKonta +=kwota
            print("DEALER MA WIĘCEJ NIZ 21 PUNKTÓW, WYGRAŁEŚ!")
            ktosWygral = True
        elif punktacjaGracza > 21:
            stanKonta -=kwota
            print("MASZ WIĘCEJ NIŻ 21 PUNKTÓW, PRZEGRAŁEŚ")
            ktosWygral = True
        else:
            if czySkonczyles == False:
                print("Czy chcesz dobrać kolejną kartę? [dobierz/zostaw]")
                dobieranie = str(input())
                if dobieranie == 'dobierz':
                    kartyGracza = dobieranieKarty(karty, kartyGracza)
                    punktacjaGracza, punktacjaDealera = punktacjaKart(kartyGracza, kartyDealera)
                elif dobieranie == 'zostaw':
                    czySkonczyles = True
                else:
                    print("Niepoprawne slowo, wpisz dobierz dla dobrania karty lub zostaw dla skończenia")
            else:
                while punktacjaDealera <= punktacjaGracza and punktacjaDealera < 21:
                    kartyDealera = dobieranieKarty(karty, kartyDealera)
                    punktacjaGracza, punktacjaDealera = punktacjaKart(kartyGracza, kartyDealera)
                if punktacjaDealera > punktacjaGracza and punktacjaDealera <= 21:
                    print("Karty dealera to:")
                    for i in range(len(kartyDealera)):
                        print(kartyDealera[i][1] + " " + kartyDealera[i][0])
                    print("(Punktacja kart: " + str(punktacjaDealera) + ")")
                    print(" ")
                    print("Karty gracza to:")
                    for i in range(len(kartyGracza)):
                        print(kartyGracza[i][1] + " " + kartyGracza[i][0])
                    print("(Punktacja kart: " + str(punktacjaGracza) + ")")
                    stanKonta -=kwota
                    print("DEALER MA WIĘCEJ PUNKTÓW NIŻ TY I MNIEJ NIŻ 22, PRZEGRAŁEŚ")
                    ktosWygral = True
    wybor = False    
    while  wybor == False:
        if stanKonta == 0:
            doWidzenia(stanKonta,True)
        ponownaGra = int(input("Czy chciałbyś zagrać ponownie? Wpisz 1 jeżeli tak lub 0 jeżeli chcesz wrócić do menu gier"))
        if ponownaGra == 1:
            blackjackWprowadzenie(stanKonta)
        elif ponownaGra == 0:
            menuGier(stanKonta)
        else:
            print("Błędne wprowadzenie, wprowadź 1 aby rozpocząć nową grę lub 0 aby wrócić do menu gier")


def blackjackWprowadzenie(stanKonta):
    karty = {'Serce': {'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False, 'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False, 'Król': False, 'As': False}, 'Piki':{'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False, 'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False, 'Król': False, 'As': False}, 'Trefle':{'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False, 'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False, 'Król': False, 'As': False},'Kiery':{'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False, 'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False, 'Król': False, 'As': False}}
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
        rundaBlackjack(stanKonta,karty)
    else:
        menuGier(stanKonta)

def menuGier(stanKonta):
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
            blackjackWprowadzenie(stanKonta)
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
            doWidzenia(stanKonta, czyWKasynie)
            prawidlowyWybor = True
        else:
            print("Bledny wybor sprobuj ponownie ")

def doWidzenia(stanKonta, bylWKasynie):
    print("Do widzenia! Do zobaczenia następnym razem!")
    if bylWKasynie == True:
        if stanKonta == 0:
            print("Twoj stan konta wynosi 0 więc wypadasz z kasyna, do zobaczenia!")
        else:
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
            doWidzenia(0, czyWKasynie)
            break
        else:
            blad()
    if tak == True:
        stanKonta = float(1000)
        menuGier(stanKonta)
        
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
            doWidzenia(0, czyWKasynie)
            break
        else:
            blad()
    if pelnoletni == True:
        czyChceszWejsc()

print("Witaj w kasynie W&W")
czyWKasynie = False
czyPelnoletni()
