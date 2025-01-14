from um import count

def test_count():

    assert count('Um, I am Haris') == 1
    assert count('Um , Um') == 2
    assert count('Hello, um, World') == 1
    assert count('Yummy, Tummy ummm um and sum') == 1
    assert count('um, um, UM, Um, uM') == 5