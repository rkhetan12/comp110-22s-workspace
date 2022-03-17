# """An example of for in syntax."""

# from xxlimited import new


# names: list[str] = ["Kris", "Kaki", "Ezri", "Macr"]

# # Example of iterating through names using a while loop
# print("whole output")
# i: int = 0
# while i < len(names):
#     name: str = names[i]
#     print(name)
#     i += 1

# print("for..in output.")
# # The following for..in loop is the same as the while loop
# for name in names:
#     print(name)

# for n in range(2, 10):
#     print(n)


# m: int = 2
# while m < 10:
#     print(m)
#     m = m + 1


def filter_by_last(given_list: list[str], one_character: str) -> list[str]:
    new_list: list[str] = list()
    i: int = 0
    p: int = 0
    TempStr: str = ""
    while i < len(given_list):
        # TempStr = given_list[i]
        # p = len(TempStr) - 1
        # if one_character == TempStr[p]:
        #     new_list.append(given_list[i])

        if one_character in given_list[i][len(given_list[i]) - 1]:
            new_list.append(given_list[i])
        i += 1

        # if one_character in given_list[i]:
        #     #if one_character in given_list[i][len(given_list[i]) - 1]:
        #     p = 0
        #     while (p < len(given_list[i]):
        #         if p == len(given_list[i]) -1
        #             if one_character == given_list[i][p]




        #    # print (len(given_list[i])-1)
        #         new_list.append(given_list[i])
        # i = i + 1
    return new_list


print(filter_by_last(["apple", "orange", "banaena"], "a"))
    