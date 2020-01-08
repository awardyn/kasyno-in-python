import random


def sprawdzaniepozycji(pozycja, tab):
    x = pozycja
    if pozycja == 0:
        y = len(tab) - 1
        z = pozycja + 1
    elif pozycja == len(tab) - 1:
        z = 0
        y = pozycja - 1
    else:
        y = pozycja - 1
        z = pozycja + 1
    return x, y, z


def wygrana(symbole_i_wartosci, lista_bonusow, lista_kluczy, i, suma, dodatkowy_rzut):
    if lista_kluczy[i] == 'bonus':
        bonus = random.choice(lista_bonusow)
        if bonus == 'wygrana 10x':
            suma = suma + 10
        elif bonus == 'wygrana 3x':
            suma = suma + 3
        else:
            dodatkowy_rzut = True
    else:
        wartosc = symbole_i_wartosci[lista_kluczy[i]]
        suma = suma + wartosc
    return suma, dodatkowy_rzut


def ruchAutomatu(symbole_i_wartosci, lista_bonusow, lista_kluczy):
    i1b, i2b, i3b, i3, i3a, i2a, i2, i1, i1a = int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0)
    pierwszaKolumna = random.choice(lista_kluczy)
    drugaKolumna = random.choice(lista_kluczy)
    trzeciaKolumna = random.choice(lista_kluczy)
    for i in range(len(lista_kluczy)):
        if lista_kluczy[i] == pierwszaKolumna:
            i1, i1b, i1a = sprawdzaniepozycji(i, lista_kluczy)
        if lista_kluczy[i] == drugaKolumna:
            i2, i2b, i2a = sprawdzaniepozycji(i, lista_kluczy)
        if lista_kluczy[i] == trzeciaKolumna:
            i3, i3b, i3a = sprawdzaniepozycji(i, lista_kluczy)

    print(str(lista_kluczy[i1b]) + " " + str(lista_kluczy[i2b]) + " " + str(lista_kluczy[i3b]))
    print(" ")
    print(str(lista_kluczy[i1]) + " " + str(lista_kluczy[i2]) + " " + str(lista_kluczy[i3]))
    print(" ")
    print(str(lista_kluczy[i1a]) + " " + str(lista_kluczy[i2a]) + " " + str(lista_kluczy[i3a]))
    print(" ")

    ilosc_wygranych = int(0)
    suma = int(0)
    dodatkowy_rzut = False
    if lista_kluczy[i1b] == lista_kluczy[i2] and lista_kluczy[i1b] == lista_kluczy[i3a]:
        ilosc_wygranych += 1
        suma, dodatkowy_rzut = wygrana(symbole_i_wartosci, lista_bonusow, lista_kluczy, i2, suma, dodatkowy_rzut)
    if lista_kluczy[i1a] == lista_kluczy[i2] and lista_kluczy[i1a] == lista_kluczy[i3b]:
        ilosc_wygranych += 1
        suma, dodatkowy_rzut = wygrana(symbole_i_wartosci, lista_bonusow, lista_kluczy, i2, suma, dodatkowy_rzut)
    if lista_kluczy[i1b] == lista_kluczy[i2b] and lista_kluczy[i1b] == lista_kluczy[i3b]:
        ilosc_wygranych += 1
        suma, dodatkowy_rzut = wygrana(symbole_i_wartosci, lista_bonusow, lista_kluczy, i1b, suma, dodatkowy_rzut)
    if lista_kluczy[i1] == lista_kluczy[i2] and lista_kluczy[i1] == lista_kluczy[i3]:
        ilosc_wygranych += 1
        suma, dodatkowy_rzut = wygrana(symbole_i_wartosci, lista_bonusow, lista_kluczy, i1, suma, dodatkowy_rzut)
    if lista_kluczy[i1a] == lista_kluczy[i2a] and lista_kluczy[i1a] == lista_kluczy[i3a]:
        ilosc_wygranych += 1
        suma, dodatkowy_rzut = wygrana(symbole_i_wartosci, lista_bonusow, lista_kluczy, i1a, suma, dodatkowy_rzut)
    return suma * ilosc_wygranych, dodatkowy_rzut
