"""Tests for the function."""

__author__ = "730476155"

from dictionary import invert, count
from exercises.ex06.dictionary import favorite_color


def test_invert_empty() -> None:
    """Test will return out a blank dictionary (edge case)."""
    input_dictionary: dict[str, str] = {}
    assert invert(input_dictionary) == {}


def test_invert_5_character_str() -> None:
    """Test will invert 5 character strings (use case)."""
    input_dictionary: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input_dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_5_word_str() -> None:
    """Test will invert 5 word strings (use case)."""
    input_dictionary: dict[str, str] = {'little': 'big', 'time': 'clock', 'sunny': 'cloudy', 'funny': 'sad', 'lime': 'lemon'}
    assert invert(input_dictionary) == {'big': 'little', 'clock': 'time', 'cloudy': 'sunny', 'sad': 'funny', 'lemon': 'lime'}


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


def test_favorite_color_empty() -> None:
    """Test will return out an empty string (edge case)."""
    names_and_fav_colors: dict[str, str] = {}
    assert favorite_color(names_and_fav_colors) == ""


def test_favorite_color_multiple() -> None:
    """Test will return out the highest color value string (use case)."""
    names_and_fav_colors: dict[str, str] = {'i': 'Green', 'a': 'Yellow', 'b': 'Blue', 'c': 'Yellow', 'd': 'Blue', 'e': 'Blue', 'f': 'Purple', 'g': 'Yellow', 'h': 'Blue', 'k': 'Yellow'}
    assert favorite_color(names_and_fav_colors) == "Yellow"


def test_favorite_color_highesr_color_value() -> None:
    """Test will return the highest color value string using a dictionary (use case)."""
    names_and_fav_colors: dict[str, str] = {'Ria': 'Blue', 'Sneha': 'Yellow', 'Mom': 'Blue', 'Dad': 'Purple'}
    assert favorite_color(names_and_fav_colors) == "Blue"