import wspolneFunkcje
import koloRuletka
import blackjack
import automat

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
    assert automat.wygrana({"arbuz": 1, "pomarancz": 1, "truskawka": 1, "siodemka": 2, "bonus": "bonus", "winogrona": 1, "malina": 1, "dziesiatka": 2, "czeresnia": 1}, ['dodatkowy rzut', 'wygrana 10x', 'dodatkowy rzut', 'dodatkowy rzut', 'dodatkowy rzut', 'wygrana 3x', 'wygrana 3x'], ["arbuz", "pomarancz", "truskawka", "siodemka", "bonus", "winogrona", "malina", "dziesiatka", "czeresnia"], 0, 0, False) == (1, False)
    assert automat.wygrana({"arbuz": 1, "pomarancz": 1, "truskawka": 1, "siodemka": 2, "bonus": "bonus", "winogrona": 1, "malina": 1, "dziesiatka": 2, "czeresnia": 1}, ['dodatkowy rzut', 'dodatkowy rzut', 'dodatkowy rzut', 'dodatkowy rzut'], ["arbuz", "pomarancz", "truskawka", "siodemka", "bonus", "winogrona", "malina", "dziesiatka", "czeresnia"], 4, 10, False) == (10, True)
