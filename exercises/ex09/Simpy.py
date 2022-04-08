"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730476155"


class Simpy:
    """Writing a utility class called Simpy that is helpful for working with sequences of numerical data."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Its purpose is to initialize the `values` attribute of the newly constructed `Simpy` object to the argument passed in."""
        self.values = values

    def __str__(self) -> str:
        """Method will automagically be called when a `Simpy` object is converted to a `str` representation."""
        return f"Simpy({self.values})"

    def fill(self, value: float, number_of_ints: int) -> None:
        """Method will fill a Simpy's value with a specific number of repeating values."""
        self.values.clear()
        i: int = 0
        while i < number_of_ints:
            self.values.append(value)
            i = i + 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Method will produce a list of values except the last item in the list."""
        self.values.clear()
        assert step != 0.0
        if step > 0.0:
            i: float = start
            while i < stop:
                self.values.append(i)
                i = i + step
        else:
            if step < 0.0:
                i: float = start
                while i > stop:
                    self.values.append(i)
                    i = i + step

    def sum(self) -> float:
        """Method will take in all the values and return a sum."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Method will use the addition operator to add a Simpy object to with either a float or Simpy Object."""
        resulting_list: list[float] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                resulting_list.append(self.values[i] + rhs)
                i = i + 1
        else:
            i = 0
            while i < len(self.values):
                assert len(self.values) == len(rhs.values)
                resulting_list.append(self.values[i] + rhs.values[i])
                i = i + 1
        return Simpy(resulting_list)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Method will use the power operator to power a Simpy object to with either a float or Simpy Object."""
        resulting_list: list[float] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                resulting_list.append(self.values[i] ** rhs)
                i = i + 1
        else:
            i = 0
            while i < len(self.values):
                assert len(self.values) == len(rhs.values)
                resulting_list.append(self.values[i] ** rhs.values[i])
                i = i + 1
        return Simpy(resulting_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Method will produce a mask to whether the values attribute matches the Simpy object or a float value."""
        resulting_list: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                resulting_list.append(self.values[i] == rhs)
                i = i + 1
        else:
            i = 0
            while i < len(self.values):
                assert len(self.values) == len(rhs.values)
                resulting_list.append(self.values[i] == rhs.values[i])
                i = i + 1
        return resulting_list

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Method will produce a mask to whether the values attribute is greater than the Simpy object or a float value."""
        resulting_list: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                resulting_list.append(self.values[i] > rhs)
                i = i + 1
        else:
            i = 0
            while i < len(self.values):
                assert len(self.values) == len(rhs.values)
                resulting_list.append(self.values[i] > rhs.values[i])
                i = i + 1
        return resulting_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Method will allow for the ability to use subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            resulting_list: Simpy = Simpy([])
            i = 0
            assert len(self.values) == len(rhs)
            while i < len(self.values):
                if rhs[i]:
                    resulting_list.values.append(self.values[i])
                i += 1
            return resulting_list