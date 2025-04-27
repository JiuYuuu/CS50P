from bank import value

def test_greeting():
    assert value("hello") == 0
    assert value(" Hello") == 0
    assert value("hi") == 20
    assert value("CS50") == 100
