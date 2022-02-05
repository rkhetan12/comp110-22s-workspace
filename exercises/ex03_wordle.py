"""Creating Wordle, just like the real one while giving the player six guesses."""

__author__ = "730476155"

secret_word: str = "codes"


def contains_char(string_to_be_guessed: str, character_found_in_guess: str) -> bool:
    """Returns the True if the single character is found anywhere in the guess."""
    i: int = 0
    assert len(character_found_in_guess) == 1
    while i < len(string_to_be_guessed):
        if string_to_be_guessed[i] == character_found_in_guess:
            return True
        i += 1
    return False


def emojified(guess_string: str, secret_word: str) -> str:
    """The purpose of the emojofied function is to have two strings that are equal in length and codify it using the green, yellow, and white emojies."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    resulting_emoji: str = ""
    i: int = 0
    assert len(guess_string) == len(secret_word)
    while i < len(secret_word):
        if guess_string[i] == secret_word[i]:
            resulting_emoji = resulting_emoji + GREEN_BOX
        elif contains_char(secret_word, guess_string[i]):
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
        i += 1
    return resulting_emoji


def input_guess(expected_length: int) -> str:
    """The purpose of the input_guess fucnction is to hvae an expected length of the guess in the parameter, and the user will keep guessing until they provide a guess of the same length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    length_of_secret_word: int = len(secret_word)
    you_guessed_it: bool = False
    while turns <= 6 and you_guessed_it is False:
        print(f"=== Turn {turns}/6 === ")
        guess: str = input_guess(length_of_secret_word)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turns}/6 turns! ")
            you_guessed_it = True
        turns += 1

    if turns > 6:
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()