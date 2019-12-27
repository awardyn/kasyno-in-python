import random
import time

def sprawdzeniewyniku(wynik, ruletka):
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
    return parzystosc, kolor, tuzin

def krecenieKolem():
    zmienna = 3
    wynik = random.randint(0, 37)
    while zmienna > 0:
        print(str(zmienna) + "...")
        time.sleep(2)
        zmienna -= 1
    return wynik