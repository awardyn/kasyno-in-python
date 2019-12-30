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


def losowanieLiczby():
    liczba = random.randint(1, 90)
    return liczba