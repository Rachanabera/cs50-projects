import pytest
from twttr import shorten

def test_shortened_word():
    assert shorten("Hello World") == "Hll Wrld"

def test_empty_string():
    assert shorten("") == ""

def test_all_vowels():
    assert shorten("aeiou") == ""

def test_mixed_case_vowels():
    assert shorten("AeIoU") == ""

def test_no_vowels():
    assert shorten("bcd") == "bcd"

def test_mixed_characters():
    assert shorten("CS50 is awesome!") == "CS50 s wsm!"
