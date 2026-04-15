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
    assert add(2, 2) == 4, "Function did not return 4"
    print("Test BASIC ADDITION")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4, "Function did not return 4"
    assert add_with_bug(0, 0) == 0
    print("Test BASIC ADDITION PASSED (does it mean code ok?)")
    #assert add_with_bug(6, 7) == 13 #will fail here

#дублирование логики
def test_addition_dublicated():
    assert add(2,3) == 2+3 #предполагается что этот плюс не используется в той функции

def test_addition_overcomplicated():
    #formal valid test but too slow
    for  i in range(0, 2**32):
        for j in range(0, 2**32): 
            assert add(i,j) == sum([i, j])  #не должны использовать все наборы входных параметров
            assert add(-i, -j) == sum([-i,-j])
            assert add(-i, j) == sum([-i,j])
            assert add(i, -j) == sum([i,-j])

def test_addition_reasonable():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13 #will fail here
    assert add(6, -7) == -1
    assert add(-7, 0) == -7
    assert add(7, 0) == 7
    print("Test ADDITION REASONABLE PASS")

def test_addition_commutative():
    #can be in previous test but logically separated
    assert add(7,-6) == 1
    assert add(-6,7) == 1

def test_tax_calculation_pesticised():
    #using only integers limits test case
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30.0
    assert calculate_tax_with_bug(0) == 0.0
    print("Test TAX_CALCULATION PASSED")
    #must fails with float but i did not used them
    #assert calculate_tax_with_bug(24.5) == 3.67 3.675

def test_tax_calculation():
    #using only integers limits test case
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(245) == 36.75
    assert calculate_tax_with_bug(-200) == -30.0
    assert calculate_tax_with_bug(0) == 0.0
    #using floats make additional test case not available
    assert calculate_tax_with_bug(24.5) == 3.67 # 3.675
    print("Test TAX_CALCULATION PASSED")
    
if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_dublicated()
    #test_addition_overcomplicated()
    test_addition_reasonable()
    test_addition_commutative()
    test_tax_calculation_pesticised()
    test_tax_calculation()