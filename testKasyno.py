import wspolneFunkcje
import koloRuletka
import blackjack


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
