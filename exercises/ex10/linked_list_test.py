"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, is_equal, scale


__author__ = "730476155"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """When the list is empty, the Linked List should rase an index error."""
    with pytest.raises(IndexError):
        value_at(None, 5)


def test_value_at_index_zero() -> None:
    """When the first index is 0. Return the data of the current Node being processed on the list."""
    index = 0
    assert value_at(Node(8, None), index)


def test_value_at_first_index() -> None:
    """When the first index is 1. Return the data of the current Node being processed on the list."""
    index = 1
    assert value_at(Node(10, Node(20, Node(30, None))), index)


def test_max_empty() -> None:
    """If the linked List is empty, should raise a value error."""
    with pytest.raises(ValueError):
        max(None)


def test_max_case_words() -> None:
    """The linked case will cause the maximum value as output."""
    linked_list = max(Node(10, Node(30, Node(20, None))))
    assert linked_list == 30


def test_linkify_example() -> None:
    """The linkify list will result in 10 -> 20 -> 30 -> None."""
    linked_list = Node(10, Node(30, Node(20, None)))
    array_list = [10, 30, 20]
    result = linkify(array_list)
    assert is_equal(result, linked_list)


def test_linkify_empty() -> None:
    """The linkify list will result in None."""
    array_list = []
    assert linkify(array_list) is None


def test_scale_empty() -> None:
    """The result will be None."""
    N = None
    assert is_equal(scale(N, 2), None)


def test_scale_multiply() -> None:
    """The result will multiply each node."""
    N2 = linkify([6, 4, 2])
    N = linkify([3, 2, 1])
    assert is_equal(scale(N, 2), N2)
    