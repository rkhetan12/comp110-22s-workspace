"""Tests for the function."""

__author__ = "730476155"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test will return out a blank list (edge case)."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_mix_and_odd() -> None:
    """Test will return only evens from a mix of odd and even list (use case)."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_only_evens_mix_and_odd_reverse() -> None:
    """Test will return only evens and from a mix of odd and even list reverse (use case)."""
    xs: list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert only_evens(xs) == [10, 8, 6, 4, 2]


def test_concat_empty() -> None:
    """Test will return out a blank list (edge case)."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_linear_numbers() -> None:
    """Test will return the first list followed by the second list (use case)."""
    first_list: list[int] = [1, 2, 3, 4]
    second_list: list[int] = [5, 6, 7, 8]
    assert concat(first_list, second_list)


def test_concat_mixed_odd_and_even_numbers() -> None:
    """Test will return the first list followed by the second list (use case)."""
    first_list: list[int] = [1, 3, 4, 5]
    second_list: list[int] = [6, 7, 2, 8]
    assert concat(first_list, second_list)


def test_sub_doubles() -> None:
    """Test will return only one number in list (use case)."""
    xs: list[int] = [10, 20]
    beginning_index: int = 0
    end_index: int = 1
    assert sub(xs, beginning_index, end_index) == [10]


def test_sub_multiples() -> None:
    """Test will return only two number in list (use case)."""
    xs: list[int] = [10, 20, 30, 40]
    beginning_index: int = 1
    end_index: int = 3
    assert sub(xs, beginning_index, end_index) == [20, 30]


def test_sub_single_case() -> None:
    """Test will return no number in list (edge case)."""
    xs: list[int] = [10]
    beginning_index: int = 0
    end_index: int = 0
    assert sub(xs, beginning_index, end_index) == []


def test_sub_empty_case() -> None:
    """Test will return no number in list (edge case)."""
    xs: list[int] = []
    beginning_index: int = 5
    end_index: int = -1
    assert sub(xs, beginning_index, end_index) == []