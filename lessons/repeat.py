
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
    i: int = 0
    new_str: str = "\""
    while i < len(word_of_any_length):
        if single_character == word_of_any_length[i]:
            new_str = new_str + str(i)
        i = i + 1
    new_str = new_str + "\""
    return new_str


print(indices_of("wowow", "w"))
