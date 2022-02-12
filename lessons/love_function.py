"""Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(strvar1: str, n: int) -> str:
    """Generates a string that reoeats a loving message in times."""
    love_note: str = ""
    counter: int = 0
    while counter < n:
        love_note += love(strvar1) + "\n"
        counter += 1
    return love_note

print(spread_love("Goodbye", 2))