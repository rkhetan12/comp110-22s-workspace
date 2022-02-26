"""Where function skeletons and implementations will take place."""

__author__ = "730476155"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Function takes the keys of the input list and those key becomes the values of the output list and vice versa."""
    reverse_dictionary: dict[str, str] = {}
    for key in input_dict:
        first_new: str = input_dict[key]
        if first_new not in reverse_dictionary:
            reverse_dictionary[first_new] = key
        else:
            raise KeyError("Error message: More than one key of the same")
    return reverse_dictionary


# print(invert({'a': 'z', 'b': 'y', 'c': 'x'})) 


def count(list_of_items: list[str]) -> dict[str, int]:
    """Function count will return a value associated with times a value is called for."""
    new_dictionary: dict[str, int] = {}
    for item in list_of_items: 
        if item in new_dictionary:
            new_dictionary[item] += 1
        else:
            new_dictionary[item] = 1
    return new_dictionary


# print(count(["blue", "yellow", "green", "yellow"]))


def favorite_color(names_and_fav_colors: dict[str, str]) -> str:
    """Function will return the color that appears most frequently. If there is a tie for a color, the function will return the color that appeared first in the dictionary."""
    temp_dictionary: dict[str, int] = {}
    for item in names_and_fav_colors:
        if names_and_fav_colors[item] in temp_dictionary:
            temp_dictionary[names_and_fav_colors[item]] += 1
        else:
            temp_dictionary[names_and_fav_colors[item]] = 1
    i: int = 0
    new_string: str = ""
    for key in temp_dictionary:
        if temp_dictionary[key] > i:
            i = temp_dictionary[key]
            new_string = key
    return new_string

# print(favorite_color({'i': 'Green', 'a': 'Yellow', 'b': 'Blue', 'c': 'Yellow', 'd': 'Blue', 'e': 'Blue', 'f': 'Purple', 'g': 'Yellow', 'h': 'Blue', 'k': 'Yellow'}))