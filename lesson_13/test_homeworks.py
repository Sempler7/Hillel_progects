import pytest

#роверяем функцию: sum_numbers()
from homeworks import sum_numbers

def test_sum_positive_numbers():
    assert sum_numbers(2, 3) == 5

def test_sum_negative_numbers():
    assert sum_numbers(-2, -3) == -5

def test_sum_zero():
    assert sum_numbers(0, 0) == 0

def test_sum_mixed_signs():
    assert sum_numbers(-5, 10) == 5

#роверяем функцию: calculate_tax()
from homeworks import calculate_tax

def test_low_income_tax():
    assert calculate_tax(9000) == 900.00  # 10%

def test_middle_income_tax():
    assert calculate_tax(30000) == 4500.00  # 15%

def test_high_income_tax():
    assert calculate_tax(600000) == 120000.00  # 20%


#роверяем функцию: Triangle()
from homeworks import Triangle

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert t.area() == 6.0

def test_triangle_perimetr():
    t = Triangle(3, 4, 5)
    assert t.perimetr() == 12

def test_format_integer():
    t = Triangle(3, 4, 5)
    assert t.format_number(6.0) == "6"

def test_format_float():
    t = Triangle(3, 4, 5)
    assert t.format_number(6.25) == "6.25"

def test_str_output_simple():
    t = Triangle(3, 4, 5)
    assert str(t) == "Area: 6, Perimeter: 12"

def test_str_output_precision():
    t = Triangle(3, 4.2, 5.8)
    assert str(t) == "Area: 6.50, Perimeter: 13"

def test_triangle_edge_case():
    t = Triangle(0, 0, 0)
    assert t.area() == 0.0
    assert t.perimetr() == 0
    assert str(t) == "Area: 0, Perimeter: 0"
