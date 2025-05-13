import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("hey") == 20
    assert value("Hey") == 20

def test_other():
    assert value("wassup") == 100
    assert value("WASSUP") == 100
