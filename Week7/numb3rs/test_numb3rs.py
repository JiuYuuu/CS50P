from numb3rs import validate

def test_ipv4():
    assert validate("hello") == False
    assert validate("192.168.1.1.1") == False
    assert validate("256.255.255.255") == False
    assert validate("255.255.0") == False
    assert validate("255.256.265.0") == False
    assert validate("10.0.") == False

    assert validate("192.168.10.0") == True
    assert validate("10.0.0.1") == True
    assert validate("100.20.20.0") == True
    assert validate("255.255.255.255") == True
