import pytest
from bank import value

def test_hello():
    assert value("hello") == 0

def test_hello_with_caps():
    assert value("Hello") == 0

def test_h_only():
    assert value("hi") == 20

def test_h_only_caps():
    assert value("Hi") == 20

def test_other_greetings():
    assert value("Good morning") == 100

def test_non_h_greetings():
    assert value("What’s up?") == 100

def test_hello_with_other_chars():
    assert value("Hello there") == 0
