import random
import time


def krecenieKolem():
    zmienna = 3
    wynik = random.randint(0,37)
    while zmienna > 0:
        print(str(zmienna) + "...")
        time.sleep(2)
        zmienna -=1
    return wynik