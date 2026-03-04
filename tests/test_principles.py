import sys
sys.path.append("../src")

#TODO make it with `pip install -e .`

from math_demo import add

def test_principles():
    assert add(2, 2) == 4
    print("Test BASIC ADDITIONS")

if __name__ == "__main__":
    test_principles()