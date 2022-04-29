# """Utility functions for working with Linked Lists."""

# from __future__ import annotations
# from typing import Optional

# __author__ = "730476155"


# class Node:
#     """An item in a singly-linked list."""
#     data: int
#     next: Optional[Node]

#     def __init__(self, data: int, next: Optional[Node]):
#         """Construct a singly linked list. Use None for 2nd argument if tail."""
#         self.data = data
#         self.next = next

#     def __str__(self) -> str:
#         """Produce a string visualization of the linked list."""
#         if self.next is None:
#             return f"{self.data} -> None"
#         else:
#             return f"{self.data} -> {self.next}"

    
# def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
#     """Test if two linked lists are deeply (values and order) equal to one another."""
#     if lhs is None and rhs is None:
#         return True
#     elif lhs is None or rhs is None or lhs.data != rhs.data:
#         return False
#     else:
#         return is_equal(lhs.next, rhs.next)


# def last(head: Optional[Node]) -> int:
#     """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
#     if head is None:
#         raise ValueError("last cannot be called with None")
#     else:
#         if head.next is None:
#             return head.data
#         else:
#             return last(head.next)


# def value_at(head: Optional[Node], index: int) -> int:
#     """Return the data of the Node stored at the given index, or raise an IndexError if the index does not exist."""
#     if head is None:
#         raise IndexError("Index is out of bounds on the list.")
#     if (index != 0):
#         return value_at(head.next, (index - 1))
#     else:
#         return head.data


# def max(head: Optional[Node]) -> int:
#     """Given a head Node, return the maximim data value in the linked list. If the linked list is empty, raise a ValueError."""
#     if head is None:
#         raise ValueError("Cannot call max with None.")
#     if head.next is None:
#         return head.data
#     else:
#         i: int = max(head.next)
#         if head.data > i:
#             return head.data
#         else:
#             return i


# def linkify(items: list[int]) -> Optional[Node]:
#     """Given a list[int], your linkify function should return a Linked List of Nodes with the same values, in the same order, as the input list."""
#     if items == []:
#         return None
#     else:
#         return Node(items[0], linkify(items[1:]))


# def scale(head: Optional[Node], factor: int) -> Optional[Node]:
#     """Given a head Node of a linked list and a int factor to scale by, return a new linked list of Nodes where each value in the original list is scaled (multiplied) by the scaling factor."""
#     if head is None:
#         return None
#     else:
#         return Node((head.data * factor), scale(head.next, factor))


# def Ria(value: int):
#     if(value < 1):
#         return;
#     Ria(value - 1);
#     print(value) 
#     return

# # Ria(10)


# def factorial(x: int) -> int:
#     """This is a recursive function
#     to find the factorial of an integer"""
#     print(x)
#     if x == 1:
#         return 1
#     else:
#         y: int = factorial(x - 1)
#         return (x * y)


# my_answer: int = factorial(10)
# print("The factorial of", 10, "is", my_answer)


from xml.etree.ElementTree import ProcessingInstruction


def multiples(given_list: list[int]) -> list[bool]:
    new_bool_list: list[bool] = []
    i: int = 0
    if given_list[i] % given_list[len(given_list) - 1] == 0:
        new_bool_list.append(True)
    else:
        new_bool_list.append(False)
    i = i + 1
    while i < len(given_list):
        if given_list[i] % given_list[i - 1] == 0:
            new_bool_list.append(True)
        else:
            new_bool_list.append(False)
        i += 1
    return new_bool_list


# print(multiples([2, 3, 4, 8, 16, 2, 4, 2]))


def reverse_multiply(given_list: list[int]) -> list[int]:
    new_list: list[int] = []
    i: int = len(given_list) - 1
    while i >= 0:
        new_list.append(given_list[i] * 2)
        i = i - 1
    return new_list


# print(reverse_multiply([1, 2, 3]))

def free-biscuits(given_dict: dict[str, list[int]]) -> dict[str, bool]:
    new_dict: dict[str, bool] = dict()
    for games in given_dict:
        total: int = 0
        for points in given_dict[games]:
            total = total + points
        if total >= 100:
            new_dict[games] = True
        else:
            new_dict[games] = False
    return new_dict

print(free)

