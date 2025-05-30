from um import count


def test_count():
    assert count("CS50P") == 0
    assert count("yummy") == 0
    assert count("umum") == 0

    assert count("CS50P, um") == 1
    assert count("um um um") == 3
    assert count("um?") == 1
    assert count("Um, yummy") == 1
    assert count("Um, yummy, um...") == 2
