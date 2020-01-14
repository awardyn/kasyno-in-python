import koloRuletka
import wspolneFunkcje
import automat
import blackjack
import bingo
import time


def dodawanieNowychKart(karty, kartyGracza, kartyDealera, czySkonczyles, punktacjaGracza, punktacjaDealera):
    print("Czy chcesz dobrać kolejną kartę? [dobierz/zostaw]")
    dobieranie = str(input())
    if dobieranie == 'dobierz':
        kartyGracza = wspolneFunkcje.dobieranieKarty(karty, kartyGracza)
        punktacjaGracza, punktacjaDealera = blackjack.punktacjaKart(kartyGracza, kartyDealera)
    elif dobieranie == 'zostaw':
        czySkonczyles = True
    else:
        print("Niepoprawne slowo, wpisz dobierz dla dobrania karty lub zostaw dla skończenia")
    return kartyGracza, punktacjaGracza, punktacjaDealera, czySkonczyles



def kwotaDoObstawienia(stanKonta):
    kwotaWprowadzona = False
    kwota = float(0)
    while not kwotaWprowadzona:
        kwota = float(
            input("Wprowadz kwotę jaką chcesz obstawić. Dostępny jest przedział od 0 do " + str(stanKonta) + " "))
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

    # TU ZNAJDUJE SIE PETLA ZAGNIEZDZONA
    for i in range(2):
        wspolneFunkcje.dobieranieKarty(karty, kartyGracza)
        wspolneFunkcje.dobieranieKarty(karty, kartyDealera)
    # -----------------------------------------------------

    punktacjaGracza, punktacjaDealera = blackjack.punktacjaKart(kartyGracza, kartyDealera)
    ktosWygral = False
    czySkonczyles = False
    while not ktosWygral:
        blackjack.wypisanieKart(kartyDealera, kartyGracza, punktacjaGracza, punktacjaDealera)

        if punktacjaGracza == 21 and punktacjaDealera == 21:
            print("REMIS")
            ktosWygral = True
        elif punktacjaGracza == 21:
            print("MASZ BLACKJACKA WYGRAŁEŚ " + str(kwota * 2) + "!")
            stanKonta += kwota
            ktosWygral = True
        elif punktacjaDealera == 21:
            stanKonta -= kwota
            print("DEALER MA BLACKJACKA, PRZEGRAŁEŚ " + str(kwota) + "!")
            ktosWygral = True
        elif punktacjaDealera > 21:
            stanKonta += kwota
            print("DEALER MA WIĘCEJ NIZ 21 PUNKTÓW, WYGRAŁEŚ " + str(kwota * 2) + "!")
            ktosWygral = True
        elif punktacjaGracza > 21:
            stanKonta -= kwota
            print("MASZ WIĘCEJ NIŻ 21 PUNKTÓW, PRZEGRAŁEŚ " + str(kwota) + "!")
            ktosWygral = True
        else:
            if not czySkonczyles:
                kartyGracza, punktacjaGracza, punktacjaDealera, czySkonczyles = dodawanieNowychKart(
                    karty, kartyGracza, kartyDealera, czySkonczyles, punktacjaGracza, punktacjaDealera)
            if czySkonczyles:
                punktacjaGracza, punktacjaDealera, karty, kartyDealera, kartyGracza, stanKonta, ktosWygral = blackjack.poskonczeniudodawania(
                    punktacjaGracza, punktacjaDealera, karty, kartyDealera, kartyGracza, stanKonta, kwota, ktosWygral)

    ponownaGra = wspolneFunkcje.ponowneRozpoczecie(stanKonta)
    if ponownaGra == "1":
        blackjackWprowadzenie(stanKonta)
    else:
        menuGier(stanKonta)


def rundaRuletki(stanKonta, ruletka):
    cyfry = []
    wybor = str("")
    wyborl = str("")
    for i in range(37):
        cyfry.append(str(i))
    koloRuletka.mozliwosciDoWyboru(ruletka)
    poprawnieWybrane = False
    while not poprawnieWybrane:
        wybor = input()
        wyborl = wybor.lower()
        if wybor in cyfry or wyborl == 'parzyste' or wyborl == 'nieparzyste' or wyborl == 'czerwone' or wyborl == 'czarne' or wyborl == 'pierwszy tuzin' or wyborl == 'drugi tuzin' or wyborl == 'trzeci tuzin':
            poprawnieWybrane = True
        else:
            print("Błędny wybór, proszę wprowadzić poprawną nazwę")
    kwota = kwotaDoObstawienia(stanKonta)
    wynik = koloRuletka.krecenieKolem()
    print("Wypadło " + str(wynik))

    parzystosc, kolor, tuzin = koloRuletka.sprawdzeniewyniku(wynik, ruletka)
    if str(wynik) == wybor or kolor == wybor.lower() or parzystosc == wybor.lower() or wybor.lower() == tuzin:
        if wybor in cyfry:
            print("Gratulacje wygrałeś " + str(36 * kwota))
            stanKonta += 35 * kwota
        elif wyborl == 'parzyste' or wyborl == 'nieparzyste' or wyborl == 'czarne' or wyborl == 'czerwone':
            print("Gratulacje wygrałeś " + str(2 * kwota))
            stanKonta += kwota
        else:
            print("Gratulacje wygrałeś " + str(3 * kwota))
            stanKonta += 2 * kwota
    else:
        print("Niestety przegrałeś " + str(kwota))
        stanKonta -= kwota
    ponownaGra = wspolneFunkcje.ponowneRozpoczecie(stanKonta)
    if ponownaGra == "1":
        ruletkaWprowadzenie(stanKonta)
    else:
        menuGier(stanKonta)


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
    if mnoznik == 0 and darmowy_rzut is False:
        print("Niestety nic nie wygrałeś tym razem! Spróbuj ponownie")
        stanKonta = stanKonta - kwota
    elif mnoznik != 0 and darmowy_rzut is False:
        print("Wygrałeś " + str(kwota * mnoznik) + "!!")
        stanKonta = stanKonta - kwota
        stanKonta = stanKonta + kwota * mnoznik
    elif mnoznik == 0 and darmowy_rzut:
        print("Udalo ci sie wygrac darmowy rzut, aby go wykorzystac musisz ponownie od razu zagrać, "
              "inaczej przepadnie! Kwota obstawiona przechodzi z tej na nastepna runde! Jezeli zrezygnujesz to nie "
              "stracisz pieniedzy!")
    else:
        print("Wygrałeś " + str(kwota * mnoznik) + "!! Dodatkowo udalo ci sie wygrac darmowy rzut, aby go wykorzystac "
                                                   "musisz ponownie od razu zagrać, inaczej przepadnie! Kwota "
                                                   "obstawiona przechodzi z tej na nastepna runde! Jezeli zrezygnujesz "
                                                   "to nie stracisz pieniedzy!")
        stanKonta = stanKonta + kwota * mnoznik

    ponownaGra = wspolneFunkcje.ponowneRozpoczecie(stanKonta)
    if ponownaGra == "1":
        automatWprowadzenie(stanKonta, kwota, darmowy_rzut)
    else:
        menuGier(stanKonta)


def rundaBingo90(stanKonta, planszaGracza, planszeKomputera, liczby):
    kwota = kwotaDoObstawienia(stanKonta)

    wierszeGracza, kolumnyGracza, kK, wK = bingo.tworzenieTabelWynikow()

    print("Zaczynamy gre w Bingo! Co 2 sekundy bedzie losowana jedna liczba z zakresu od 1 do 90 przy czym bedziesz "
          "dostawac informacje czy ktorys z graczy trafil liczbe. Wygrywa ta osoba, ktora trafi pierwsza caly wiersz/ "
          "kolumne!")
    print(" ")
    print("Twoja plansza wyglada nastepujaco")
    bingo.wypisanieplanszy(planszaGracza)
    for i in range(len(planszaGracza)):
        wiersz = ""
        for j in range(len(planszaGracza[i])):
            wiersz = wiersz + str(planszaGracza[i][j]) + " "
        print(wiersz)
    poprawne = False
    while not poprawne:
        rozpoczecieBingo = str(input("Wpisz t po przeczytaniu zasady! "))
        if rozpoczecieBingo != "t":
            print("Niepoprawna wartosc, wpisz t aby rozpoczac!")
        else:
            poprawne = True
    print("Zaczynamy!")
    print(" ")
    wygrana = False
    while not wygrana:
        for i in range(2):
            print(str(2 - i) + "...")
            time.sleep(1)
        liczba, liczby = bingo.losowanieLiczby(liczby)
        print("Wypadlo " + str(liczba) + "!")
        wygrana, stanKonta, wierszeGracza, kolumnyGracza = bingo.sprawdzenieLiczby(kwota, liczba, stanKonta,
                                                                                   planszaGracza, wierszeGracza,
                                                                                   kolumnyGracza, wygrana)
        if not wygrana:
            for b in range(3):
                wygrana, stanKonta, wK, kK = bingo.sprawdzenieLiczbyKomputer(kwota, liczba, stanKonta,
                                                                             planszeKomputera[b], wK, kK, b, wygrana)
    ponownaGra = wspolneFunkcje.ponowneRozpoczecie(stanKonta)
    if ponownaGra == "1":
        bingo90Wprowadzenie(stanKonta)
    else:
        menuGier(stanKonta)


def blackjackWprowadzenie(stanKonta):
    karty = {'Serce': {'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False,
                       'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False,
                       'Król': False, 'As': False},
             'Piki': {'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False,
                      'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False,
                      'Król': False, 'As': False},
             'Trefle': {'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False,
                        'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False,
                        'Król': False, 'As': False},
             'Kiery': {'Dwa': False, 'Trzy': False, 'Cztery': False, 'Pięć': False, 'Sześć': False, 'Siedem': False,
                       'Osiem': False, 'Dziewięć': False, 'Dziesięć': False, 'Walet': False, 'Dama': False,
                       'Król': False, 'As': False}}

    zeroJeden = wspolneFunkcje.rozpoczecie()
    if zeroJeden == "1":
        rundaBlackjack(stanKonta, karty)
    else:
        menuGier(stanKonta)


def ruletkaWprowadzenie(stanKonta):
    ruletka = {'Czerwone': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
               'Czarne': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]}

    zeroJeden = wspolneFunkcje.rozpoczecie()
    if zeroJeden == "1":
        rundaRuletki(stanKonta, ruletka)
    else:
        menuGier(stanKonta)


def automatWprowadzenie(stanKonta, kwota, darmowy_rzut):
    symbole_i_wartosci = {"arbuz": 1, "pomarancz": 1, "truskawka": 1, "siodemka": 2, "bonus": "bonus", "winogrona": 1,
                          "malina": 1, "dziesiatka": 2, "czeresnia": 1}
    lista_bonusow = ['dodatkowy rzut', 'wygrana 10x', 'dodatkowy rzut', 'dodatkowy rzut', 'dodatkowy rzut',
                     'wygrana 3x', 'wygrana 3x']
    lista_kluczy = ["arbuz", "pomarancz", "truskawka", "siodemka", "bonus", "winogrona", "malina", "dziesiatka",
                    "czeresnia"]

    zeroJeden = wspolneFunkcje.rozpoczecie()
    if zeroJeden == "1":
        rundaAutomatu(stanKonta, symbole_i_wartosci, lista_bonusow, lista_kluczy, darmowy_rzut, kwota)
    else:
        menuGier(stanKonta)


def bingo90Wprowadzenie(stanKonta):
    # TU SIE ZNADUJA DWIE TABLICE ZAGNIEZDZONE
    liczby = []
    for i in range(1, 91):
        liczby.append(i)
    planszaBingo90 = bingo.tworzeniePlanszy()
    planszeK = []
    for i in range(3):
        plansza = bingo.tworzeniePlanszy()
        planszeK.append(plansza)
    zeroJeden = wspolneFunkcje.rozpoczecie()
    if zeroJeden == "1":
        rundaBingo90(stanKonta, planszaBingo90, planszeK, liczby)


def menuGier(stanKonta):
    print("Menu Gier")
    print("Twoj aktualny stan konta to " + str(stanKonta) + ". W co chciałbyś aktualnie zagrać?")
    listaGier = ['blackjacka', 'ruletkę', 'automat', 'bingo90']
    for i in range(len(listaGier)):
        print("Jeżeli chcesz zagrać w " + listaGier[i] + " wybierz " + str(i + 1))
    print("Jeżeli chcesz wyjść z kasyna wybierz 0")
    prawidlowyWybor = False
    while not prawidlowyWybor:
        wybor = str(input())
        if wybor == "1":
            print("Witamy w grze blackjack")
            blackjackWprowadzenie(stanKonta)
            prawidlowyWybor = True
        elif wybor == "2":
            print("Witamy w grze ruletka")
            ruletkaWprowadzenie(stanKonta)
            prawidlowyWybor = True
        elif wybor == "3":
            print("Witamy w grze na automacie")
            automatWprowadzenie(stanKonta, 0, False)
            prawidlowyWybor = True
        elif wybor == "4":
            print("Witamy w grze bingo")
            bingo90Wprowadzenie(stanKonta)
            prawidlowyWybor = True
        elif wybor == "0":
            wspolneFunkcje.doWidzenia(stanKonta, True)
            prawidlowyWybor = True
        else:
            print("Bledny wybor sprobuj ponownie ")


def czyChceszWejsc(wKasynie, stan):
    tak = False
    while not tak:
        wejscie = str(input("Czy jestes pewien, ze chcesz rzucic sie w wir szaleństwa kasynowego? [T/N] "))
        if wejscie == "T":
            print("Super! Zaczynajmy!")
            tak = True
        elif wejscie == "N":
            print("Szkoda!")
            wspolneFunkcje.doWidzenia(0, wKasynie)
            break
        else:
            blad()
    if tak:
        menuGier(stan + 50.0)


def blad():
    print("Błąd wprowadzenia, powtórz, wpisując T dla tak lub N dla nie")


def czyPelnoletni(wKasynie, stan):
    pelnoletni = False
    while not pelnoletni:
        pelnoletnosc = str(input("Czy jesteś pełnoletni? [T/N] "))
        if pelnoletnosc == "T":
            print("Super, czyli możesz wejść do kasyna!")
            pelnoletni = True
        elif pelnoletnosc == "N":
            print("Niestety musisz opuścić ten lokal")
            wspolneFunkcje.doWidzenia(0, wKasynie)
            break
        else:
            blad()
    czyChceszWejsc(wKasynie, stan)

with open("stanKonta.txt", "r") as f:
    doOdczytu = f.read()
    stanKonta = float(doOdczytu)
f.close()
print("Witaj w kasynie W&W")
czyWKasynie = False
czyPelnoletni(czyWKasynie, stanKonta)
