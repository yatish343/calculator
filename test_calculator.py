import sys
import os

# Add the directory containing app.py to the system path
sys.path.append(os.path.dirname(__file__))

import app as calculator  # Import your calculator functions from app.py

def test_add():
    assert calculator.add(5, 2) == 7

def test_subtract():
    assert calculator.subtract(5, 2) == 3

def test_multiply():
    assert calculator.multiply(5, 2) == 10

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(10, 0) == "Error: Division by zero"
