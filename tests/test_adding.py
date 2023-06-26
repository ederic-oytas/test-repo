from test_oyster import add


def test_add():
    assert add(1, 2) == 3
    assert add(20, 25) == 45
    assert add(1000, 2500) == 3500
