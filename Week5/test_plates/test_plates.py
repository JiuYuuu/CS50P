from plates import is_valid
def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEFG") == False
    assert is_valid("123456") == False
    assert is_valid("CS5.0") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS05") == False
    assert is_valid("CS5P0") == False
    assert is_valid("CS50P") == False
    assert is_valid("HELLO") == True
