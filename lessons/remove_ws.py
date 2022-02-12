# def remove_ws(wrd: str) -> str:
#     """Removes white space."""
#     new_word: str = ""
#     i: int = 0
#     while i < len(wrd):
#         if wrd[i] != " ":
#             new_word = new_word + wrd[i]
#         i += 1
#     return new_word

# clean_word: str = ""
# raw_word: str = "    Ria Ria   "
# clean_word = remove_ws(raw_word)
# print(clean_word)

def remove_lws(wrd: str) -> str:
    """Removes leading white space."""
    new_word: str = ""
    i: int = 0
    while i < len(wrd):
        if wrd[i] != " ":
            while i < len(wrd):
                new_word = new_word + wrd[i]
                i += 1
        i += 1
    return new_word

def remove_tws(wrd: str) -> str:
    """Removes trailing white space."""
    new_word: str = ""
    print(len(wrd))
    i: int = len(wrd) - 1
    while i > -1:
        if wrd[i] != " ":
            while i > -1:
                new_word = wrd[i] + new_word
                i -= 1
        i -= 1
    print(len(new_word))
    return new_word


# raw_word: str = "    Ria Ria   "
# clean_word: str = remove_lws(remove_tws(raw_word))
# print(remove_lws(remove_tws(raw_word)))
print(remove_lws(remove_tws("    Ria Ria   ")))