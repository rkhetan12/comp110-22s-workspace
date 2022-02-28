"""Example of writing a functon to search a list."""


# def main() -> None:
#     guess: str = input("WHat is the code word?")
#     possible_answers: list[str] = ["pokemon", "wordle"]
#     if contains(guess, possible_answers):
#         print("We're letting you in the secret code...")
#     else:
#         print("Go back to Davis")


# def contains(needle: str, haystack: list[str]) -> bool:
#     """Test if needle is found in haystack."""
#     for item in haystack:
#         if item == needle:
#             return True
#     return False


# print(__name__)

# if __name__ == "__main__":
#     main()


def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i += 1
    return False
        

        
print(contains("sneha", ["one", "two", "sneha"]))