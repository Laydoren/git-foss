import sys
sys.path.append("../src")

#TODO make it with `pip install -e .`

from math_demo import (
    add,
    add_with_bug,
    calculate_tax_with_bug,
    calculate_tax
)

def test_addition():
    assert add(2, 2) == 4, "Function should return 4"
    print("Test BASIC ADDITIONS PASSED")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4, "Function should return 4"
    assert add_with_bug(0, 0) == 0
    print("Test BASIC ADDITIONS WITH BUG PASSED")
    # assert add_with_bug(6, 7) == 13 # Ты дурак?

def test_addition_duplicated():
    # is it real good test (relies on absence of + in add())
    assert add(2, 3) == 2 + 3

def test_addition_overcomplicated():
    #formally valid test but too slow
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == sum([i, j])
            assert add(-i, j) == sum([-i, j])
            assert add(i, -j) == sum([i, -j])
            assert add(-i, -j) == sum([-i, -j])

def test_addition_reasonable():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13
    assert add(-6, -7) == -13
    assert add(6, -7) == -1
    assert add(-7, 0) == -7
    assert add(7, 0) == 7
    print("Test BASIC REASONABLE PASSED")

def test_addition_commutative():
    # can be previous test but logically separated
    assert add(7, -6) == 1
    assert add(-6, 7) == 1
    print("Test BASIC COMMUTATIVE PASSED")

def test_tax_calculation_pesticised():
    # using only integers limits test case
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30.
    assert calculate_tax_with_bug(0) == 0.
    print("Test BASIC TAX PASSED")
    # fails next
    #assert calculate_tax_with_bug(24.5) == 3.67

def test_tax_calculation():
    # using only integers limits test case
    assert calculate_tax(1000) == 150.0
    assert calculate_tax(100) == 15.0
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(245) == 36.75
    assert calculate_tax(-200) == -30.
    assert calculate_tax(0) == 0.
    assert calculate_tax(24.5) == 3.67
    print("Test BASIC TAX PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    # test_addition_overcomplicated()
    test_addition_reasonable()
    test_addition_commutative()
    test_tax_calculation_pesticised()
    test_tax_calculation()