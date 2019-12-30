import wspolneFunkcje
import koloRuletka
import blackjack
import automat
import bingo


def testkwotaDoObstawienia():
    assert type([]) == type(wspolneFunkcje.dobieranieKarty({'Serce': {'Dwa': False, 'Trzy': False, 'Cztery': False,
                                                                      'Pięć': False, 'Sześć': False, 'Siedem': False,
                                                                      'Osiem': False, 'Dziewięć': False,
                                                                      'Dziesięć': False, 'Walet': False, 'Dama': False,
                                                                      'Król': False, 'As': False},
                                                            'Piki': {'Dwa': False, 'Trzy': False, 'Cztery': False,
                                                                     'Pięć': False, 'Sześć': False, 'Siedem': False,
                                                                     'Osiem': False, 'Dziewięć': False,
                                                                     'Dziesięć': False, 'Walet': False, 'Dama': False,
                                                                     'Król': False, 'As': False},
                                                            'Trefle': {'Dwa': False, 'Trzy': False, 'Cztery': False,
                                                                       'Pięć': False, 'Sześć': False, 'Siedem': False,
                                                                       'Osiem': False, 'Dziewięć': False,
                                                                       'Dziesięć': False, 'Walet': False, 'Dama': False,
                                                                       'Król': False, 'As': False},
                                                            'Kiery': {'Dwa': False, 'Trzy': False, 'Cztery': False,
                                                                      'Pięć': False, 'Sześć': False, 'Siedem': False,
                                                                      'Osiem': False, 'Dziewięć': False,
                                                                      'Dziesięć': False, 'Walet': False, 'Dama': False,
                                                                      'Król': False, 'As': False}}, []))


def testpunktacjaKart():
    assert blackjack.punktacjaKart([['Trefle', 'As'], ['Serce', 'Dama']],
                                   [['Kiery', 'Dwa'], ['Piki', 'Osiem']]) == (21, 10)
    assert blackjack.punktacjaKart([['Kiery', 'Trzy'], ['Piki', 'Walet'], ['Kiery', 'As']],
                                   [['Kiery', 'Dwa'], ['Piki', 'Osiem']]) == (14, 10)


def testpunkty():
    assert blackjack.punkty('Dwa') == 2
    assert blackjack.punkty('As') == 1


def testkrecenieKolem():
    assert type(koloRuletka.krecenieKolem()) == type(1)


def testdobieranieKarty():
    assert wspolneFunkcje.dobieranieKarty({'Kiery': {'Dwa': False}}, []) == [['Kiery', 'Dwa']]


def testwygrana():
    assert automat.wygrana(
        {"arbuz": 1, "pomarancz": 1, "truskawka": 1, "siodemka": 2, "bonus": "bonus", "winogrona": 1, "malina": 1,
         "dziesiatka": 2, "czeresnia": 1},
        ['dodatkowy rzut', 'wygrana 10x', 'dodatkowy rzut', 'dodatkowy rzut', 'dodatkowy rzut', 'wygrana 3x',
         'wygrana 3x'],
        ["arbuz", "pomarancz", "truskawka", "siodemka", "bonus", "winogrona", "malina", "dziesiatka", "czeresnia"], 0,
        0, False) == (1, False)
    assert automat.wygrana(
        {"arbuz": 1, "pomarancz": 1, "truskawka": 1, "siodemka": 2, "bonus": "bonus", "winogrona": 1, "malina": 1,
         "dziesiatka": 2, "czeresnia": 1}, ['dodatkowy rzut', 'dodatkowy rzut', 'dodatkowy rzut', 'dodatkowy rzut'],
        ["arbuz", "pomarancz", "truskawka", "siodemka", "bonus", "winogrona", "malina", "dziesiatka", "czeresnia"], 4,
        10, False) == (10, True)


def testsprawdzenieWyniku():
    assert koloRuletka.sprawdzeniewyniku(10, {
        'Czerwone': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
        'Czarne': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]}) == (
               'parzyste', 'czarne', 'pierwszy tuzin')
    assert koloRuletka.sprawdzeniewyniku(27, {
        'Czerwone': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
        'Czarne': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]}) == (
               'nieparzyste', 'czerwone', 'trzeci tuzin')


def testlosowanieLiczby():
    assert type(bingo.losowanieLiczby([1, 2, 3, 4, 5, 6, 7, 8])) == type(())


def testtworzeniePlanszy():
    assert type(bingo.tworzeniePlanszy()) == type([])
