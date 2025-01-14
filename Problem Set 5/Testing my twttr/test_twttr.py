from twttr import shorten

def test_shorten():
    assert shorten('haris') == 'hrs'
    assert shorten('ali') == 'l'
    assert shorten('elephant') == 'lphnt'
    assert shorten('uganda') == 'gnd'
    assert shorten('bcdfgh') == 'bcdfgh'
    assert shorten('AJKEIO') == 'JK'
    assert shorten('43JKL') == '43JKL'
    assert shorten('HarIs!!') == 'Hrs!!'

if __name__ == '__main__':
    test_shorten()
    print('All tests passed !!')