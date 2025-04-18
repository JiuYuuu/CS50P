from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HEllO") == "Hll"
    assert shorten("CS50P") == "CS50P"
    assert shorten("CS50!") == "CS50!"
    assert shorten("") == ""

