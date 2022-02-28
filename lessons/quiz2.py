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


def vowels_and_threes(given_str: str) -> str:
    """Function that takes in an index that is a multiple of 3 or a vowel (one or the other, not both)."""
    new_string: str = ""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    i: int = 0
    
    while i < len(given_str):
        if (i % 3 == 0 and given_str[i] in vowels):
            new_string = new_string + ""
        # elif (i % 3 == 0 or given_str[i] in vowels):
        #     new_string = new_string + given_str[i]
        elif i % 3 == 0:
            new_string = new_string + given_str[i]
        elif given_str[i] == vowels[0]:
            new_string = new_string + given_str[i]
        elif given_str[i] == vowels[1]:
            new_string = new_string + given_str[i]
        elif given_str[i] == vowels[2]:
            new_string = new_string + given_str[i]
        elif given_str[i] == vowels[3]:
            new_string = new_string + given_str[i]
        elif given_str[i] == vowels[4]:
            new_string = new_string + given_str[i]
        i += 1
    return new_string


print(vowels_and_threes("comp110"))
print(vowels_and_threes("hello world"))
print(vowels_and_threes("aeiou"))


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