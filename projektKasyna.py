def menuGier():
    print(stanKonta)

def doWidzenia():
    print("Do widzenia! Do zobaczenia następnym razem!")
def czyChceszWejsc():
    tak = False
    while tak == False:
        wejscie = str(input("Czy jestes pewien, ze chcesz rzucic sie w wir szaleństwa kasynowego? [T/N] "))
        if wejscie == "T":
            print("Super! Zaczynajmy!")
            tak = True
        elif wejscie == "N":
            print("Szkoda!")
            doWidzenia()
            break
        else:
            blad()
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
            doWidzenia()
            break
        else:
            blad()
    czyChceszWejsc()


print("Witaj w kasynie W&W")
stanKonta = float(1000)
czyPelnoletni()
