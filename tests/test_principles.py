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


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()