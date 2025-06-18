from calculator import *

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(3, 7) == -4


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

def test_square_root():
    assert square_root(9) == 3
    assert square_root(16) == 4
