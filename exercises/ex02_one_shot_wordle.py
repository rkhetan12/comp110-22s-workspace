"""Ex02 - One Short Wordle - An improvement of Ex01 where the player will have the guess a secret word."""

__author__ = "730476155"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(secret_word) != len(guess):
    guess: str = input(f"That was not {len(secret_word)}! Try again: ")

i: int = 0
resulting_emoji: str = " "
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

to_keep_track_of: bool = False
alternate_indices: int = 0

while i < len(secret_word):
    if guess[i] == secret_word[i]:
        resulting_emoji = resulting_emoji + GREEN_BOX 
    else:
        while to_keep_track_of is False and alternate_indices < len(secret_word):
            if guess[i] == secret_word[alternate_indices]:
                resulting_emoji = resulting_emoji + YELLOW_BOX
                to_keep_track_of = True
            alternate_indices = alternate_indices + 1
        if to_keep_track_of is False:
            resulting_emoji = resulting_emoji + WHITE_BOX
        to_keep_track_of = False
        alternate_indices = 0
      
    i = i + 1
print(resulting_emoji)

if secret_word == guess:
    print("Woo! You got it!")
else:
    if len(secret_word) == len(guess) and secret_word != guess:
        print("Not quite. Play again soon!")