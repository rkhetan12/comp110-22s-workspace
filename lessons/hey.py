def make_word(root: list[str]) -> str:
    word: str = ""
    i: int = 0
    while i < len(root):
        if i % 2 == 0:
            word += root[i]
        else:
            if len(word) < 5:
                word += root[i]
            else:
                return word
        i += 1
        
    return word


def main() -> None:
    """Entry point of program."""
    strings: list[str] = ["hey", "o", "eh", "e"]
    word: str = make_word(strings)
    print(word)


if __name__ == "__manin__":
    main()

print(word)