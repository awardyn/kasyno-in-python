def menuGier():
    czyWKasynie = True
    print("Twoj aktualny stan konta to " + str(stanKonta) + ". W co chciałbyś aktualnie zagrać?")
    listaGier = ['abc','bcd','cde','def','efg']
    for i in range(len(listaGier)):
        print("Jeżeli chcesz zagrać w " + listaGier[i] + " wybierz " + str(i+1))
    print("Jeżeli chcesz wyjść z kasyna wybierz 0")
    prawidlowyWybor = False
    while prawidlowyWybor == False:
        wybor = int(input())
        if wybor == 1:
            print("1")
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
            doWidzenia(czyWKasynie)
            prawidlowyWybor = True
        else:
            print("Bledny wybor sprobuj ponownie ")

def doWidzenia(bylWKasynie):
    print("Do widzenia! Do zobaczenia następnym razem!")
    if bylWKasynie == True:
        print("Twoj stan konta po wyjsciu wynosi " + str(stanKonta))
def czyChceszWejsc():
    tak = False
    while tak == False:
        wejscie = str(input("Czy jestes pewien, ze chcesz rzucic sie w wir szaleństwa kasynowego? [T/N] "))
        if wejscie == "T":
            print("Super! Zaczynajmy!")
            tak = True
        elif wejscie == "N":
            print("Szkoda!")
            doWidzenia(czyWKasynie)
            break
        else:
            blad()
    if tak == True:
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
            doWidzenia(czyWKasynie)
            break
        else:
            blad()
    if pelnoletni == True:
        czyChceszWejsc()


print("Witaj w kasynie W&W")
stanKonta = float(1000)
czyWKasynie = False
czyPelnoletni()
