# Kasyno
Gra kasyno pozwalająca online zagrać w wybrane gry bez użycia realnych pieniedzy. Wykonana jest na potrzeby projektu na zajecia ze wstepu do programowania

© copyright imie nazwisko
## Start
Aby rozpoczac gre nalezy wlaczyc plik projektKasyna.py

### Przyklad w programie JetBrains PyCharm Community Edition

```
File > Open > project-python> projektKasyna.py > Run
```

## Testowanie
Aby wlaczyc testy do projektu nalezy skorzystac z programu pytest

### Instalacja pytest

* Zainstaluj [pytest](https://docs.pytest.org/en/latest/getting-started.html)
    *  W terminalu wpisz:
        ```
        pip install -U pytest
        ```
    *  Aby sprawdzic poprawnosc wersji wpisz:
        ```
        pytest --version
        ```

#### Konfiguracja pytest w JetBrains PyCharm Community Edition

Aby skonfigurowac interpretera uruchamiajacego testy:
```
File → Settings → Tools → Python Integrated Tools → W Default test runner wybierz pytest → OK.
```

### Uruchamianie testow

* Linia polecen
    ```
    pytest testKasyno.py
    ```
UWAGA! plik musi mieć rozszerzenie *.py

* PyCharm
    ```
    Kliknij prawym przyciskiem na skrypt → Run 'nazwa'.
    ```
