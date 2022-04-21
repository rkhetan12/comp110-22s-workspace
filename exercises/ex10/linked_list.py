"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = 730476155


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

    
def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Return the data of the Node stored at the given index, or raise an IndexError if the index does not exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if (index != 0):
        return value_at(head.next, (index - 1))
    else:
        return head.data


def max(head: Optional[Node]) -> int:
    """Given a head Node, return the maximim data value in the linked list. If the linked list is empty, raise a ValueError."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    if head.next is None:
        return head.data
    else:
        i: int = max(head.next)
        if head.data > i:
            return head.data
        else:
            return i


def linkify(items: list[int]) -> Optional[Node]:
    """Given a list[int], your linkify function should return a Linked List of Nodes with the same values, in the same order, as the input list."""
    
    



    



# class Basket:
#     eggs: list[str]

#     def same_color(self, another_eggs_basket: Basket) -> bool:
#         result: bool = False
#     #     colors: list[str] = ["red", "orange", "yellow"]
#     #     i: int = 0
#     #     while i < len(colors):
#     #         if colors[i] in self.eggs and another_eggs_basket:
#     #             result = True
#     #         i = i + 1
#         return result
