import sys
sys.path.append("../src")

#TODO make it with `pip install -e .`

from math_demo import (
    add,
    add_with_bug
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


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    # test_addition_overcomplicated()
    test_addition_reasonable()
    test_addition_commutative()