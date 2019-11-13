print("Witaj w kasynie W&W")
pelnoletnosc = str(input("Czy jesteś pełnoletni? [T/N]" ))
if pelnoletnosc == "T":
    print("Super")
elif pelnoletnosc == "N":
    print("Niestety musisz opuścić ten lokal")
else:
    print("Powtórz, wpisując T dla tak lub N dla nie")
