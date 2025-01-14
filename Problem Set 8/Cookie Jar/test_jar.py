from jar import Jar


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == '🍪🍪'
    jar.deposit(7)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪'


def test_withdraw():
    jar = Jar(capacity=12)  # Default capacity is 12
    jar.deposit(9)  # Deposit 9 cookies
    jar.withdraw(7)  # Withdraw 7 cookies
    assert str(jar) == '🍪🍪'  # 9 - 7 = 2 cookies left, so jar should show 🍪🍪
    
    # Now try withdrawing more than what is available
    try:
        jar.withdraw(3)  # This should raise an error
        assert False  # Fail if no error is raised
    except ValueError:
        pass  # Test passes if ValueError is raised