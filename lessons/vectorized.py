from __future__ import annotations
from typing import ItemsView


class StrArray:
    items: list[str]

    def __init__(self, items):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: str) -> StrArray:
        """"Add is a vectorized operation that applies to all items.
        When rhs is a str, it is concatenated to every item in a new StrArray
        """
        
        # Establish a result list of strings that is empty
        result: list[str] = list()
        # Loop through every item in self.items
        for item in self.items:
            # Append the concatenation of item with rhs to your result list
            result.append(item + rhs)
        # After loop, return a new StrArray object constructed with result list
        return StrArray(result)


first: StrArray = StrArray(["Armando", " Brady", " Caleb"])
last: StrArray = StrArray(["Bacot", "Mankek", "Love"])
print(first + "!")