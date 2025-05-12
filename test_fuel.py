import pytest
from fuel import convert, gauge

# ----- Tests for convert() -----

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("0/4") == 0
    assert convert("4/4") == 100

def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_value_error_invalid_numbers():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("two/three")

def test_convert_value_error_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/4")

# ----- Tests for gauge() -----

def test_gauge_empty_and_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
