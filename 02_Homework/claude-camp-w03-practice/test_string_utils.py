import pytest

from string_utils import count_vowels, is_palindrome, reverse_words


def test_reverse_words_normal_sentence():
    assert reverse_words("hello world") == "world hello"


def test_reverse_words_removes_extra_spaces():
    assert reverse_words("  data   files  are fun  ") == "fun are files data"


def test_reverse_words_empty_string():
    assert reverse_words("") == ""


def test_reverse_words_rejects_non_string():
    with pytest.raises(TypeError):
        reverse_words(123)


def test_count_vowels_normal_text():
    assert count_vowels("Claude Camp") == 4


def test_count_vowels_handles_no_vowels():
    assert count_vowels("rhythm") == 0


def test_count_vowels_empty_string():
    assert count_vowels("") == 0


def test_count_vowels_rejects_non_string():
    with pytest.raises(TypeError):
        count_vowels(None)


def test_is_palindrome_simple_word():
    assert is_palindrome("level") is True


def test_is_palindrome_ignores_case_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") is True


def test_is_palindrome_false_case():
    assert is_palindrome("hello") is False


def test_is_palindrome_rejects_non_string():
    with pytest.raises(TypeError):
        is_palindrome(["level"])
