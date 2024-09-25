import calculator

def test_add():
    assert calculator.add(3, 2) == 5

def test_subtract():
    assert calculator.subtract(3, 2) == 1

def test_multiply():
    assert calculator.multiply(3, 2) == 6

def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(6, 0) == "Error: Division by zero"