from plates import is_valid

# Valid plate examples
def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("ABC123") == True
    assert is_valid("XY9") == True

# Invalid due to incorrect length
def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

# Invalid due to not starting with two letters
def test_invalid_start():
    assert is_valid("123ABC") == False
    assert is_valid("C1") == False
    assert is_valid("1ABC") == False

# Invalid due to zero as the first number
def test_leading_zero():
    assert is_valid("CS05") == False
    assert is_valid("AB012") == False

# Invalid due to letters after numbers
def test_letters_after_numbers():
    assert is_valid("CS50X") == False
    assert is_valid("AA1AA") == False

# Invalid due to non-alphanumeric characters
def test_invalid_characters():
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
    assert is_valid("HELLO!") == False
    assert is_valid("TEST@1") == False
