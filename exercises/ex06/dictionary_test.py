"""Tests for the function."""

__author__ = "730476155"

from dictionary import invert, count


def test_invert_empty() -> None:
    """Test will return out a blank dictionary (edge case)."""
    input_list: dict[str, str] = {}
    assert invert(input_list) == {}


def test_invert_5_character_str() -> None:
    """Test will invert 5 character strings (use case)."""
    input_list: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input_list) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_5_word_str() -> None:
    """Test will invert 5 word strings (use case)."""
    input_list: dict[str, str] = {'little': 'big', 'time': 'clock', 'sunny': 'cloudy', 'funny': 'sad', 'lime': 'lemon'}
    assert invert(input_list) == {'big': 'little', 'clock': 'time', 'cloudy': 'sunny', 'sad': 'funny', 'lemon': 'lime'}


def test_count_one_dictionary() -> None:
    """Test will return out a blank dictionary (edge case)."""
    list_of_items: list[str] = []
    assert count(list_of_items) == {}


def test_count_multiple_str() -> None:
    """Test will return out multiple strings and integers (use case)."""
    list_of_items: list[str] = ["blue", "yellow", "blue", "green", "yellow"]
    assert count(list_of_items) == {"blue": 2, "yellow": 2, "green": 1}


def test_count_multipe_str_backwards() -> None:
    """Test will return out multiple strings and integers backwards (use case)."""
    list_of_items: list[str] = ["yellow", "blue", "yellow", "green", "blue"]
    assert count(list_of_items) == {"yellow": 2, "blue": 2, "green": 1}