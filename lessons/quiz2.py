# def change_and_check(x: int, nums: list[int]) -> int:
#     """Let's see what happens!"""
#     if x < 0:
#         return 0
    
#     i: int = 0
#     while i < len(nums):
#         nums[i] += x
#         i += 1

#     i = 0
#     while i < len(nums):
#         if nums[i] == x:
#             return 0
#         i += 1
    
#     return x - 1


# def main() -> None:
#     """The entrypoint of this program."""
#     num_1: int = 0
#     list_1: list[int] = [1, 2, num_1]
#     print(list_1)
#     list_1.append(change_and_check(2, list_1))
#     print(list_1)
#     list_1.append(change_and_check(3, list_1))
#     print(list_1)


# main()

# an index that is a multiple of 3 or a vowel (one or the other, not both)


# def vowels_and_threes(given_str: str) -> str:
#     """Function that takes in an index that is a multiple of 3 or a vowel (one or the other, not both)."""
#     new_string: str = ""
#     vowels: list[str] = ["a", "e", "i", "o", "u"]
#     i: int = 0
    
#     while i < len(given_str):
#         if (i % 3 == 0 and given_str[i] in vowels):
#             new_string = new_string + ""
#         # elif (i % 3 == 0 or given_str[i] in vowels):
#         #     new_string = new_string + given_str[i]
#         elif i % 3 == 0:
#             new_string = new_string + given_str[i]
#         elif given_str[i] == vowels[0]:
#             new_string = new_string + given_str[i]
#         elif given_str[i] == vowels[1]:
#             new_string = new_string + given_str[i]
#         elif given_str[i] == vowels[2]:
#             new_string = new_string + given_str[i]
#         elif given_str[i] == vowels[3]:
#             new_string = new_string + given_str[i]
#         elif given_str[i] == vowels[4]:
#             new_string = new_string + given_str[i]
#         i += 1
#     return new_string


# print(vowels_and_threes("comp110"))
# print(vowels_and_threes("hello world"))
# print(vowels_and_threes("aeiou"))


# def dict_transform(d: dict[int, list[int]]) -> dict[int, list[int]]:

#     """Function returns the dictionary with every value in a list multiplied by its corresponding key."""
#     """return the dictionary with every value in a list multiplied by its corresponding key 2 [1, 2] -> 2 [2, 4]."""
#     int_var_1: int = 0
#     int_var_2: int = 0
#     new_dictionary: dict[int, list[int]] = {}
#     for key in d:
#         int_var_1 = key * d[key][0]
#         int_var_2 = key * d[key][1]
#         new_dictionary[key] = [int_var_1, int_var_2]
#     return new_dictionary


def dict_transform(d: dict[int, list[int]]) -> dict[int, list[int]]:

    """Function returns the dictionary with every value in a list multiplied by its corresponding key."""
    """return the dictionary with every value in a list multiplied by its corresponding key 2 [1, 2] -> 2 [2, 4]."""
    int_var_1: int = 0
    int_var_2: int = 0
    new_dictionary: dict[int, list[int]] = {}
    i: int = 0
    for key in d:
        i = 0
        while i < len(d):
            int_var_1 = key * d[key][0]
            int_var_2 = key * d[key][1]
            new_dictionary[key] = [int_var_1, int_var_2]
            i += 1
    return new_dictionary

print(dict_transform({2: [1, 2]}))


def average_grades(actual_grades: dict[str, list[int]]) -> dict[str, float]:
    """Function takes in a grades and returns out an average."""
    new_dictionary: dict[str, float] = {}
    # dividing_by: int = len(actual_grades)
    for key in actual_grades:
        total: int = 0
        for grade in actual_grades[key]:
            total = total + grade
        new_dictionary[key] = total / len(actual_grades[key])
    return new_dictionary


print(average_grades({"Emily": [75, 94, 97]}))


def odd_and_even(numbers_list: list[int]) -> list[int]:
    """Function should return a new list containing the elements that are odd and have an even index."""
    i: int = 0
    new_list: list[int] = list()
    while i < len(numbers_list):
        if numbers_list[i] % 2 == 1 and i % 2 == 0:
            new_list.append(numbers_list[i])
        i = i + 1
    return new_list


print(odd_and_even([1, 1, 1, 0, 1]))

print(odd_and_even([2, 9, 4, 17, 9, 10, 15, 13, 14, 21]))


        




























# Wrong code
#     while i < len(string):
#         if string[i] is i % 3 == 0 and vowels[i]:
#             new_string = new_string + ""
#         else:
#             if i % 3 == 0
#               new_string = new_string + string[i]
#             elif string[i] == vowels[0]:
#                 new_string = new_string + string[i]
#             elif string[i] == vowels[1]:
#                 new_string = new_string + string[i]
#             elif string[i] == vowels[2]:
#                 new_string = new_string + string[i]
#             elif string[i] == vowels[3]:
#                 new_string = new_string + string[i]
#             elif string[i] == vowels[4]:
#                 new_string = new_string + string[i]
#         i += 1

#     return new_string


# print(vowels_and_threes("110"))



