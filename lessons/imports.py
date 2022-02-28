"""Examples of importing Python."""


from lessons import helpers

# Alias a module / imported name as nother name
from lessons import helpers as hp

# Import names defined globablly in a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoing of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)

if __name__ == "__main__":
    main()