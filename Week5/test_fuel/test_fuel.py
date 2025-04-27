from fuel import convert, gauge
import pytest
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/100") == 0

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("a/c")
    with pytest.raises(ValueError):
        convert("5/1")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.2/4")
    with pytest.raises(ValueError):
        convert("1-2")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
