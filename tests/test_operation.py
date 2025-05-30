import pytest
from essential_math.operations import add, subtract, multiply, divide

def test_add():
    assert add(3, 4) == 7

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 5) == 15

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
