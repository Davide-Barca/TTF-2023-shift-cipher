import pytest
from decryption.decrypt import decrypt

def test_empty_input():
    assert decrypt("", 10) == ""

def test_key_0_same_output_as_input():
    assert decrypt("test", 0) == "test"

def test_key_1_decrypt():
    assert decrypt("bcd", 1) == "abc"

def test_key_26_same_output_as_input():
    assert decrypt("test", 26) == "test"

def test_key_13_decrypt_z():
    assert decrypt("z", 13) == "m"

def test_key_13_decrypt_a_wrap_around():
    assert decrypt("a", 13) == "n"

def test_key_5_decrypt_with_spaces():
    assert decrypt("t r l", 5) == "o m g"

def test_key_4_decrypt_with_numbers():
    assert decrypt("xiwxmrk 1 2 3 xiwxmrk", 4) == "testing 1 2 3 testing"

def test_key_21_decrypt_with_punctuation():
    assert decrypt("gzo'n zvo, bmviyhv!", 21) == "let's eat, grandma!"

def test_key_13_rotate_all_letters():
    assert decrypt("gur dhvpx oebja sbk whzcf bire gur ynml qbt.", 13) == "the quick brown fox jumps over the lazy dog."

def test_raise_value_error_for_negative_key():
    with pytest.raises(ValueError):
        decrypt("test", -1)

def test_raise_value_error_for_none_text():
    with pytest.raises(ValueError):
        decrypt(None, -1)

def test_raise_value_error_for_text_not_string():
    with pytest.raises(ValueError):
        decrypt(["test", "test"], -1)

def test_raise_value_error_for_key_not_int():
    with pytest.raises(ValueError):
        decrypt("test", "1")