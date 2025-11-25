from src.calc import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(4, 2) == 8

def test_div():
    assert div(6, 3) == 2
