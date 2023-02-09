import pytest
from encryption.encrypt import encrypt

def test_empty_input():
    assert encrypt("", 10) == ""

def test_key_0_same_output_as_input():
    assert encrypt("test", 0) == "test"

def test_key_1_encryption():
    assert encrypt("abc", 1) == "bcd"

def test_key_26_same_output_as_input():
    assert encrypt("test", 26) == "test"

def test_key_13_encrypt_m():
    assert encrypt("m", 13) == "z"

def test_key_13_encrypt_n_wrap_around():
    assert encrypt("n", 13) == "a"

def test_key_5_encrypt_with_spaces():
    assert encrypt("o m g", 5) == "t r l"

def test_key_4_encrypt_with_numbers():
    assert encrypt("testing 1 2 3 testing", 4) == "xiwxmrk 1 2 3 xiwxmrk"

def test_key_21_encrypt_with_punctuation():
    assert encrypt("let's eat, grandma!", 21) == "gzo'n zvo, bmviyhv!"

def test_key_13_rotate_all_letters():
    assert encrypt("the quick brown fox jumps over the lazy dog.", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt."

def test_raise_value_error_for_negative_key():
    with pytest.raises(ValueError):
        encrypt("test", -1)

def test_raise_value_error_for_none_text():
    with pytest.raises(ValueError):
        encrypt(None, -1)

def test_raise_value_error_for_text_not_string():
    with pytest.raises(ValueError):
        encrypt(["test", "test"], -1)

def test_raise_value_error_for_key_not_int():
    with pytest.raises(ValueError):
        encrypt("test", "1")