"""Small string utility functions for Week 3 practice."""


VOWELS = set("aeiouAEIOU")


def ensure_string(value):
    if not isinstance(value, str):
        raise TypeError("value must be a string")


def reverse_words(s):
    """Return words in reverse order while normalizing extra spaces."""
    ensure_string(s)
    return " ".join(reversed(s.split()))


def count_vowels(s):
    """Count English vowels in a string."""
    ensure_string(s)
    return sum(1 for char in s if char in VOWELS)


def is_palindrome(s):
    """Return True when text reads the same forward and backward."""
    ensure_string(s)
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
