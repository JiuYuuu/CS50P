from working import convert
import pytest


def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:10 PM to 8:10 AM") == "22:10 to 08:10"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

    with pytest.raises(ValueError):
        convert("9:66 AM to 5:66 PM")
    with pytest.raises(ValueError):
        convert("9:66 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
