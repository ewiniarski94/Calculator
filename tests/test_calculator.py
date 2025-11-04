import pytest

from src.calculator import Calculator

def test_sum():
    calc = Calculator(10, 10)
    assert calc.sum() == 20

def test_subtract():
    calc = Calculator(10, 10)
    assert calc.subtract() == 0

def test_multiply():
    calc = Calculator(10, 10)
    assert calc.multiply() == 100

def test_divide():
    calc = Calculator(10, 10)
    assert calc.divide() == 1

def test_divide_by_zero():
    calc = Calculator(10, 0)
    with pytest.raises(ZeroDivisionError):
        calc.divide()

