from bank import value

def test_if_h(): 
    v = 20
    assert value('hi') == v
    assert value('haris') == v
    assert value('HI') == v
    

def test_if_hello():
    v = 0
    assert value('hello') == v
    assert value('hello haris') == v
    assert value('HelLo') == v

def test_no_h():
    v = 100
    assert value('jdfldks') == v
    assert value('FJELSK') == v
    assert value('Dswed') == v



if __name__ == '__main__':
    test_if_h()
    test_if_hello()
    test_no_h()
    print('All tests passed!!')