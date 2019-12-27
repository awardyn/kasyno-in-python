import random
import time


def sprawdzeniewyniku(wynik, ruletka):
    tuziny = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]]
    if wynik % 2 == 0:
        parzystosc = 'parzyste'
    else:
        parzystosc = 'nieparzyste'
    if wynik in ruletka['Czerwone']:
        kolor = 'czerwone'
    elif wynik in ruletka['Czarne']:
        kolor = 'czarne'
    else:
        kolor = 'zielone'
    if wynik in tuziny[0]:
        tuzin = 'pierwszy tuzin'
    elif wynik in tuziny[1]:
        tuzin = 'drugi tuzin'
    else:
        tuzin = 'trzeci tuzin'
    return parzystosc, kolor, tuzin


def krecenieKolem():
    zmienna = 3
    wynik = random.randint(0, 37)
    while zmienna > 0:
        print(str(zmienna) + "...")
        time.sleep(2)
        zmienna -= 1
    return wynik
