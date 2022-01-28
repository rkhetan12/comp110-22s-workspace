"""Ex02 - One Short Wordle - An improvement of Ex01 where the player will have the guess a secret word."""

__author__ = "730476155"

# this part of the program lets the user guess and try again if the user inputs an incorrect number of letters
# this part of the program also allows for any word to be replaced for the secret_word and the program will still run accordingly
secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(secret_word) != len(guess):
    guess = input(f"That was not {len(secret_word)}! Try again: ")

i: int = 0
resulting_emoji: str = " "
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

to_keep_track_of: bool = False
alternate_indices: int = 0

# checking for if the index of the guess matches the index of the secret_word. If so changes the resulting_emoji changes to green
# if the current index does not match the index of the secret_word but is somewhere else in the secret_word, the resulting_emoji will change to yellow
# if the current index is no where found in the secret_word, the resulting_emoji will be white

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