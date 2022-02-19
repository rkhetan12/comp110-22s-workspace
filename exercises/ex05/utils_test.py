"""Tests for the function."""

__author__ = "730476155"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_mix_and_odd() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_only_evens_mix_and_odd_reverse() -> None:
    xs: list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert only_evens(xs) == [10, 8, 6, 4, 2]


def test_concat_empty() -> None:
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_linear_numbers() -> None:
    first_list: list[int] = [1, 2, 3, 4]
    second_list: list[int] = [5, 6, 7, 8]
    assert concat(first_list, second_list)


def test_concat_mixed_odd_and_even_numbers() -> None:
    first_list: list[int] = [1, 3, 4, 5]
    second_list: list[int] = [6, 7, 2, 8]
    assert concat(first_list, second_list)


def sub_single_test() -> None:
    # xs: list[int] = [10, 20]
    # beginning_index: int = 0
    # end_index: int = 1
    assert sub([10, 20], 0, 1) == [10]

    print(sub([10], 0, 1))