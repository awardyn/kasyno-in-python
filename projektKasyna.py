import random
import blackjack
import koloRuletka
import wspolneFunkcje
import automat

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

    
def rundaBlackjack(stanKonta, karty):
    kwota = kwotaDoObstawienia(stanKonta)
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
    punktacjaGracza, punktacjaDealera  = blackjack.punktacjaKart(kartyGracza,kartyDealera)
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
            print("MASZ BLACKJACKA WYGRAŁEŚ " + str(kwota*2) + "!")
            stanKonta +=kwota
            ktosWygral = True
        elif punktacjaDealera == 21:
            stanKonta -=kwota
            print("DEALER MA BLACKJACKA, PRZEGRAŁEŚ " + str(kwota) + "!")
            ktosWygral = True
        elif punktacjaDealera > 21:
            stanKonta +=kwota
            print("DEALER MA WIĘCEJ NIZ 21 PUNKTÓW, WYGRAŁEŚ" + str(kwota*2) + "!")
            ktosWygral = True
        elif punktacjaGracza > 21:
            stanKonta -=kwota
            print("MASZ WIĘCEJ NIŻ 21 PUNKTÓW, PRZEGRAŁEŚ " + str(kwota) + "!")
            ktosWygral = True
        else:
            if czySkonczyles == False:
                print("Czy chcesz dobrać kolejną kartę? [dobierz/zostaw]")
                dobieranie = str(input())
                if dobieranie == 'dobierz':
                    kartyGracza = wspolneFunkcje.dobieranieKarty(karty, kartyGracza)
                    punktacjaGracza, punktacjaDealera = blackjack.punktacjaKart(kartyGracza, kartyDealera)
                elif dobieranie == 'zostaw':
                    czySkonczyles = True
                else:
                    print("Niepoprawne slowo, wpisz dobierz dla dobrania karty lub zostaw dla skończenia")
            else:
                while punktacjaDealera <= punktacjaGracza and punktacjaDealera < 21:
                    kartyDealera = wspolneFunkcje.dobieranieKarty(karty, kartyDealera)
                    punktacjaGracza, punktacjaDealera = blackjack.punktacjaKart(kartyGracza, kartyDealera)
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
                    print("DEALER MA WIĘCEJ PUNKTÓW NIŻ TY I MNIEJ NIŻ 22, PRZEGRAŁEŚ " + str(kwota) + "!")
                    ktosWygral = True
    wybor = False    
    while  wybor == False:
        if stanKonta == 0:
            wspolneFunkcje.doWidzenia(stanKonta, True)
        ponownaGra = int(input("Czy chciałbyś zagrać ponownie? Wpisz 1 jeżeli tak lub 0 jeżeli chcesz wrócić do menu gier "))
        if ponownaGra == 1:
            blackjackWprowadzenie(stanKonta)
        elif ponownaGra == 0:
            menuGier(stanKonta)
        else:
            print("Błędne wprowadzenie, wprowadź 1 aby rozpocząć nową grę lub 0 aby wrócić do menu gier")


def rundaRuletki(stanKonta, ruletka):
    cyfry = []
    for i in range(37):
        cyfry.append(str(i))
    print("Wybierz co chcesz obstawić. Do wyboru masz: ")
    print("1. Numery od 0-36 (wyplata 35-1)")
    print("2. Numery parzyste/nieparzyste (wyplata 1-1)")
    print("3. Kolory czerwone/czarne (wplata 1-1)")
    print("4. Pierwszy tuzin/drugi tuzin/ trzeci tuzin (wyplata 2-1)")
    print("Kolor czerwony to liczby " + str(ruletka["Czerwone"]) + " a czarne to " + str(ruletka["Czarne"]))
    poprawnieWybrane = False
    while not poprawnieWybrane:
        wybor = input()
        if wybor in cyfry or wybor.lower() == 'parzyste' or wybor.lower() == 'nieparzyste' or wybor.lower() == 'czerwone' or wybor.lower() == 'czarne' or wybor.lower() == 'pierwszy tuzin' or wybor.lower() == 'drugi tuzin' or wybor.lower() == 'trzeci tuzin':
            poprawnieWybrane = True
        else:
            print("Błędny wybór, proszę wprowadzić poprawną nazwę")
    kwota = kwotaDoObstawienia(stanKonta)
    wynik = koloRuletka.krecenieKolem()
    print("Wypadło " + str(wynik))
    
    if wynik == 0 and wybor == '0':
        print("Gratulacje wygrałeś " + str(36*kwota))
        stanKonta +=35*kwota
    else:
        if wynik %2 == 0:
            parzystosc = 'parzyste'
        else:
            parzystosc = 'nieparzyste'
        if wynik in ruletka['Czerwone']:
            kolor = 'czerwone'
        else:
            kolor = 'czarne'
        if wynik//12 == 0:
            tuzin = 'pierwszy tuzin'
        elif wynik//12 == 1:
            tuzin = 'drugi tuzin'
        else:
            tuzin = 'trzeci tuzin'
        if wynik == wybor or kolor == wybor.lower() or parzystosc == wybor.lower() or wybor.lower() == tuzin:
            if wybor in cyfry:
                print("Gratulacje wygrałeś " + str(36*kwota))
                stanKonta += 35*kwota
            elif wybor.lower() == 'parzyste' or wybor.lower() == 'nieparzyste' or wybor.lower() == 'czarne' or wybor.lower() == 'czerwone':
                print("Gratulacje wygrałeś " + str(2*kwota))
                stanKonta += kwota
            else:
                print("Gratulacje wygrałeś " + str(3*kwota))
                stanKonta += 2*kwota
        else:
            print("Niestety przegrałeś " + str(kwota))
            stanKonta -=kwota
    wybor = False    
    while not wybor:
        if stanKonta == 0:
            wspolneFunkcje.doWidzenia(stanKonta,True)
        ponownaGra = int(input("Czy chciałbyś zagrać ponownie? Wpisz 1 jeżeli tak lub 0 jeżeli chcesz wrócić do menu gier "))
        if ponownaGra == 1:
            ruletkaWprowadzenie(stanKonta)
        elif ponownaGra == 0:
            menuGier(stanKonta)
        else:
            print("Błędne wprowadzenie, wprowadź 1 aby rozpocząć nową grę lub 0 aby wrócić do menu gier")


def rundaAutomatu(stanKonta, symbole_i_wartosci, lista_bonusow, lista_kluczy, darmowy_rzut, kwota):
    if not darmowy_rzut:
        kwota = kwotaDoObstawienia(stanKonta)
    poprawne = False
    while not poprawne:
        rozpoczecieSzufli = str(input("Wpisz t aby rozpoczac ruch maszyny! "))
        if rozpoczecieSzufli != "t":
            print("Niepoprawna wartosc, wpisz t aby rozpoczac!")
        else:
            poprawne = True
    print("")
    mnoznik, darmowy_rzut = automat.ruchAutomatu(symbole_i_wartosci, lista_bonusow, lista_kluczy)
    if mnoznik == 0 and darmowy_rzut == False:
        print("Niestety nic nie wygrałeś tym razem! Spróbuj ponownie")
        stanKonta = stanKonta - kwota
    elif mnoznik != 0 and darmowy_rzut == False:
        print("Wygrałeś " + str(kwota*mnoznik) + "!!")
        stanKonta = stanKonta - kwota
        stanKonta = stanKonta + kwota*mnoznik
    elif mnoznik == 0 and darmowy_rzut == True:
        print("Udalo ci sie wygrac darmowy rzut, aby go wykorzystac musisz ponownie od razu zagrać, "
              "inaczej przepadnie! Kwota obstawiona przechodzi z tej na nastepna runde! Jezeli zrezygnujesz to nie "
              "stracisz pieniedzy!")
    else:
        print("Wygrałeś " + str(kwota*mnoznik) + "!! Dodatkowo udalo ci sie wygrac darmowy rzut, aby go wykorzystac "
                                                 "musisz ponownie od razu zagrać, inaczej przepadnie! Kwota "
                                                 "obstawiona przechodzi z tej na nastepna runde! Jezeli zrezygnujesz "
                                                 "to nie stracisz pieniedzy!")
        stanKonta = stanKonta + kwota*mnoznik
    wybor = False
    while not wybor:
        if stanKonta == 0:
            wspolneFunkcje.doWidzenia(stanKonta, True)
        ponownaGra = int(
            input("Czy chciałbyś zagrać ponownie? Wpisz 1 jeżeli tak lub 0 jeżeli chcesz wrócić do menu gier "))
        if ponownaGra == 1:
            automatWprowadzenie(stanKonta, kwota, darmowy_rzut)
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
        rundaBlackjack(stanKonta, karty)
    else:
        menuGier(stanKonta)


def ruletkaWprowadzenie(stanKonta):
    ruletka = {'Czerwone': [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36], 'Czarne': [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]}
    rozpoczecie = False
    print("Wpisz 1 aby rozpocząć grę, lub 0 aby wyjść z niej")
    while rozpoczecie == False:
        zeroJeden = int(input())
        if zeroJeden == 1:
            rozpoczecie = True
        elif zeroJeden == 0:
            rozpoczecie = True
        else:
            print("Błędne wprowadzenie, wprowadź jeszcze raz 1 albo 0")
    if zeroJeden == 1:
        rundaRuletki(stanKonta,ruletka)
    else:
        menuGier(stanKonta)


def automatWprowadzenie(stanKonta, kwota, darmowy_rzut):
    symbole_i_wartosci = {"arbuz": 1, "pomarancz": 1, "truskawka": 1, "siodemka": 2, "bonus": "bonus", "winogrona": 1, "malina": 1, "dziesiatka": 2, "czeresnia": 1}
    lista_bonusow = ['dodatkowy rzut', 'wygrana 10x', 'dodatkowy rzut', 'dodatkowy rzut', 'dodatkowy rzut', 'wygrana 3x', 'wygrana 3x']
    lista_kluczy = ["arbuz", "pomarancz", "truskawka", "siodemka", "bonus", "winogrona", "malina", "dziesiatka", "czeresnia"]
    rozpoczecie = False
    print("Wpisz 1 aby rozpocząć grę, lub 0 aby wyjść z niej")
    while rozpoczecie == False:
        zeroJeden = int(input())
        if zeroJeden == 1:
            rozpoczecie = True
        elif zeroJeden == 0:
            rozpoczecie = True
        else:
            print("Błędne wprowadzenie, wprowadź jeszcze raz 1 albo 0")
    if zeroJeden == 1:
        rundaAutomatu(stanKonta, symbole_i_wartosci, lista_bonusow, lista_kluczy, darmowy_rzut, kwota)
    else:
        menuGier(stanKonta)


def menuGier(stanKonta):
    czyWKasynie = True
    print("Menu Gier")
    print("Twoj aktualny stan konta to " + str(stanKonta) + ". W co chciałbyś aktualnie zagrać?")
    listaGier = ['blackjacka', 'ruletkę', 'automat', 'pokera']
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
            ruletkaWprowadzenie(stanKonta)
            prawidlowyWybor = True
        elif wybor == 3:
            automatWprowadzenie(stanKonta, 0, False)
            prawidlowyWybor = True
        elif wybor == 4:
             prawidlowyWybor = True
        elif wybor == 0:
            wspolneFunkcje.doWidzenia(stanKonta, czyWKasynie)
            prawidlowyWybor = True
        else:
            print("Bledny wybor sprobuj ponownie ")


def czyChceszWejsc():
    tak = False
    while tak == False:
        wejscie = str(input("Czy jestes pewien, ze chcesz rzucic sie w wir szaleństwa kasynowego? [T/N] "))
        if wejscie == "T":
            print("Super! Zaczynajmy!")
            tak = True
        elif wejscie == "N":
            print("Szkoda!")
            wspolneFunkcje.doWidzenia(0, czyWKasynie)
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
            wspolneFunkcje.doWidzenia(0, czyWKasynie)
            break
        else:
            blad()
    if pelnoletni == True:
        czyChceszWejsc()


print("Witaj w kasynie W&W")
czyWKasynie = False
czyPelnoletni()
