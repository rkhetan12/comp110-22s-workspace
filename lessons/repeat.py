
# def repeat(long_word: str, how_many_times_repeat: int) -> str:
#     i: int = 0
#     new_str: str = ""
#     while i < len(long_word):
#         counter: int = 0
#         while counter < how_many_times_repeat:
#             new_str = new_str + long_word[i]
#             counter = counter + 1
#         i += 1

#     return new_str

# print(repeat("word", 3))


def indices_of(word_of_any_length: str, single_character: str) -> str:
    new_str: str = "\""
    i: int = 0
    while i < len(word_of_any_length):
        if word_of_any_length[i] == single_character:
            new_str = new_str + str(i)
        i = i + 1
    new_str = new_str + "\""
    return new_str

    # i: int = 0
    # new_str: str = "\""
    # while i < len(word_of_any_length):
    #     if single_character == word_of_any_length[i]:
    #         new_str = new_str + str(i)
    #     i = i + 1
    # new_str = new_str + "\""
    # return new_str


# print(indices_of("wowow", "w"))

def filter_by_last(given_list: list[str], one_letter: str) -> list[str]:
	new_list: list[str] = []
	i: int = 0
	while i < len(given_list):
		if given_list[i][len(given_list[i]) -1] == one_letter:
			new_list.append(given_list[i])
		i = i + 1
	return new_list

new_str: str = "Happy Birthday"
# print(new_str[8-1])

# print(filter_by_last(["apple", "orange", "banana"], "e"))


def grocery_shop(inventory: dict[str, int], grocery_list: dict[str, int]) -> list[str]:
    new_list: list[str] = []
    for item in grocery_list:
        print(item)
        print(inventory)
        if item in inventory:
            if inventory[item] >= grocery_list[item]:
                new_list.append(item)
    return new_list


print(grocery_shop({"bread": 3, "chips": 5, "eggs": 5}, {"chips": 5, "eggs": 5}))
    

