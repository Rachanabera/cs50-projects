from numb3rs import validate

def test_valid_addresses():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True
    assert validate("1.2.3.4") == True

def test_invalid_numbers():
    # Only one part is wrong, others are valid
    assert validate("256.0.0.1") == False
    assert validate("192.300.1.1") == False
    assert validate("192.168.1.999") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.2.300.4") == False

def test_invalid_format():
    assert validate("cat") == False
    assert validate("1234") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("...") == False
    assert validate("1..2.3") == False

def test_negative_and_text():
    assert validate("-1.2.3.4") == False
    assert validate("1.-2.3.4") == False
    assert validate("1.2.-3.4") == False
    assert validate("1.2.3.-4") == False
    assert validate("1.two.3.4") == False
