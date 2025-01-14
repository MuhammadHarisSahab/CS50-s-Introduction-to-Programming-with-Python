from plates import is_valid


def test_letters_check():
    assert is_valid('CS50') == True
    assert is_valid('CF72') == True
    assert is_valid('43KJL') == False

def test_characters_amount_check():
    assert is_valid('K') == False
    assert is_valid('KJL4324JK') == False
    assert is_valid('JK32') == True

def test_punctuation_check():
    assert is_valid('$#@') == False
    assert is_valid('CS50%') == False
    assert is_valid('CDJ543') == True

def test_numbers_check():
    assert is_valid('CS05') == False
    assert is_valid('FD546J') == False
    assert is_valid('JKL950') == True

def test_no_begin_alphabet():
        assert is_valid('43JKL') == False
        assert is_valid('5HKL') == False
        assert is_valid('4JLK43') == False
        assert is_valid('432JLK') == False
        assert is_valid('') == False
        assert is_valid('23') == False

if __name__ == '__main__':
    test_letters_check()
    test_characters_amount_check()
    test_punctuation_check()
    test_numbers_check()
    test_no_begin_alphabet()
    print('All Tests Passed!!')