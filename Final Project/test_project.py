from project import maths_facts, capital, random_memes, useful_quotes

def test_maths_facts():
    # Test with a mock year
    result = maths_facts(2021)
    assert isinstance(result, str), "maths_facts should return a string"

def test_capital():
    # Test with a mock country
    result = capital('Pakistan')
    assert isinstance(result, str), "capital should return a string"

def test_random_memes():
    # Test if the random meme is a string
    result = random_memes()
    assert isinstance(result, str), "random_memes should return a string"

def test_useful_quotes():
    # Test if the quote is a string
    result = useful_quotes()
    assert isinstance(result, str), "useful_quotes should return a string"
