import pytest
from twttr import shorten

def test_vowels():
    assert shorten("Twitter") == "Twttr"
    assert shorten("HELLO") == "HLL"
    assert shorten("tw3tt3r") == "tw3tt3r"
    assert shorten("h@ll.") == "h@ll."
