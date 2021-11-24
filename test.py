#тест
import pytest
from calculator import Calculator

cal=Calculator()

def test_addition():
    assert cal.addition(8,2) == 10
def test_subtraction():
    assert cal.subtraction(8,2)==6
def test_multiplication():
    assert cal.multiplication(8,2)==16
def test_division():
    assert cal.division(8,2)==4
def test_exponentiation():
    assert cal.exponentiation(8,2)==64