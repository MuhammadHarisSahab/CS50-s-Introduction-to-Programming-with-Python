from seasons import date_of_birth, get_mins, get_in_words

def test_date_of_birth():
    
    assert date_of_birth('2000-12-12') == '2000-12-12'

def test_get_mins():
    
    assert get_mins('2025-01-01') == 4320

def test_get_in_words():

    assert get_in_words(4320) == 'Four thousand, three hundred twenty minutes'