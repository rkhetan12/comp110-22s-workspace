"""Where function skeletons and implementations will take place."""

__author__ = "730476155"


def invert(input_list: dict[str, str]) -> dict[str, str]:
    """Function takes the keys of the input list and those key becomes the values of the output list and vice versa."""
    reverse_dictionary: dict[str, str] = {}
    for key in input_list:
        first_new: str = input_list[key]
        if first_new in reverse_dictionary:
            raise KeyError("Error message: More than one key of the same")
        reverse_dictionary[first_new] = key  
    return reverse_dictionary


print(invert({'a': 'z', 'b': 'y', 'c': 'x'})) 


def count(list_of_items: list[str]) -> dict[str, int]:
    """Function count will a value associated is the count of the number of times that value appeared in the input list."""
    new_dictionary: dict[str, int] = {}
    for item in list_of_items: 
        if item in new_dictionary:
            new_dictionary[item] += 1
        else:
            new_dictionary[item] = 1
    return new_dictionary


print(count(["blue", "yellow", "green", "yellow"]))


def favorite_color(names_and_fav_colors: dict[str, str]) -> str:
    """Function will return the color that appears most frequently. If there is a tie for a color, the function will return the color that appeared first in the dictionary."""
#     new_string: str = ""
#     i: int = 0
#     for key in names_and_fav_colors:
#         if names_and_fav_colors[key] >