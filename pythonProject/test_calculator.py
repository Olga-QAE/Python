# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, power, modulo

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4

def test_multiply():
    assert multiply(4, 2) == 8
    assert multiply(-1, -1) == 1

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    assert divide(5, 0) == "Помилка: ділення на нуль!"

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_modulo_normal():
    assert modulo(10, 3) == 1

def test_modulo_by_zero():
    assert modulo(10, 0) == "Помилка: ділення на нуль!"