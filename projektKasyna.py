def doWidzenia():
    print("Do widzenia, dziękujemy za pobyt w naszym kasynie!")

def czyPelnoletni():
    pelnoletni = False
    while pelnoletni == False:
        pelnoletnosc = str(input("Czy jesteś pełnoletni? [T/N]" ))
        if pelnoletnosc == "T":
            print("Super, czyli możesz wejść do kasyna!")
            pelnoletni = True
        elif pelnoletnosc == "N":
            print("Niestety musisz opuścić ten lokal")
            break
        else:
            print("Błąd wprowadzenia, powtórz, wpisując T dla tak lub N dla nie")


print("Witaj w kasynie W&W")
czyPelnoletni()
doWidzenia()
