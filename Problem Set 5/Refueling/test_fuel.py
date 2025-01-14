from fuel import convert, gauge

def test_convert():
    # Valid cases
    assert convert('1/2') == 50
    assert convert('2/3') == 67

    # Invalid cases
    try:
        convert('3/0')
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError"

    try:
        convert('4/3')
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'

if __name__ == "__main__":
    test_convert()
    test_gauge()
    print("All tests passed!")
