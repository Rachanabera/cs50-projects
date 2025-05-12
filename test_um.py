import um

def test_single_um():
    assert um.count("um") == 1

def test_multiple_ums():
    assert um.count("Um, thanks, um...") == 2

def test_no_um():
    assert um.count("yummy") == 0

def test_um_with_punctuation():
    assert um.count("um?") == 1
    assert um.count("Um!") == 1
    assert um.count("um.") == 1

def test_case_insensitivity():
    assert um.count("UM, thanks for the album.") == 1
    assert um.count("uM, thanks, um...") == 2

def test_empty_string():
    assert um.count("") == 0
