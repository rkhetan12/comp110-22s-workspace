"""Where function skeletons and implementations will take place."""

__author__ = "730476155"


def only_evens(xs: list[int]) -> list[int]:
    """The functions will return a list with only even numbers."""
    len_of_xs: int = len(xs)
    new_list: list[int] = list()
    # i: int = 0
    # while i < len_of_xs:
    #     if xs[i] % 2 == 0:
    #         new_list.append(xs[i])
    #     i += 1
    # return new_list

    for i in range(0, len_of_xs):
        if xs[i] % 2 == 0:
            new_list.append(xs[i])
    return new_list

    
# print(only_evens([1, 2, 3]))
# print(only_evens([1, 5, 3]))
# print(only_evens([4, 5, 6, 7, 8, 9, 10]))


# def sub(xs: list[int], beginning_index: int, end_index: int) -> list[int]:
#     """The function will generate a list between the specified start index and the end of the index -1."""
#     new_list: list[int] = list()
#     i: int = beginning_index
#     while i < end_index:
#         new_list.append(xs[i])
#         i += 1
#     return new_list

# print(sub([10, 20, 30, 40], 1, 3))

def sub(xs: list[int], beginning_index: int, end_index: int) -> list[int]:
    """The function will generate a list between the specified start index and the end of the index -1."""
    new_list: list[int] = list()
    i: int = beginning_index
    if i < 0:
        i = 0
    if end_index > len(xs):
        end_index = len(xs)
    if len(xs) == 0 or beginning_index > len(xs) or end_index <= 0:
        return new_list
    while i < end_index:
        new_list.append(xs[i])
        i += 1
    return new_list


print(sub([10, 20, 30, 40], 1, 3))


def concat(first_list: list[int], second_list: list[int]):
    """The function will generate a new list which contains all of the elements of the first list followed by all the elements of the second list."""
    new_list: list[int] = list()
    i: int = 0
    while i < len(first_list):
        new_list.append(first_list[i])
        i += 1
    i = 0
    while i < len(second_list):
        new_list.append(second_list[i])
        i += 1
    return new_list


print(concat([1, 2, 3, 4], [5, 6, 7, 8]))