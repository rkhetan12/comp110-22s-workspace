"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730476155"

five_character_word: str = input("Enter a 5-character word")

if len(five_character_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(five_character_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character_in_word: str = input("Enter a single character")

if len(single_character_in_word) > 1:
    print("Error: Character must be a single character")
    exit()
if len(single_character_in_word) == 0:
    print("Error: Character must be a single character")
    exit()
      
count_for_instances_of_similarity: int = 0

print("Enter a 5-character word: " + five_character_word)
print("Enter a single character: " + single_character_in_word)
print("Searching for " + single_character_in_word + " in " + five_character_word)

if single_character_in_word == five_character_word[0]:
    print(single_character_in_word + " found at index 0")
    count_for_instances_of_similarity = count_for_instances_of_similarity + 1
else:
    if single_character_in_word == five_character_word[1]:
        print(single_character_in_word + " found at index 1")
        count_for_instances_of_similarity = count_for_instances_of_similarity + 1
    if single_character_in_word == five_character_word[2]:
        print(single_character_in_word + " found at index 2")
        count_for_instances_of_similarity = count_for_instances_of_similarity + 1
    if single_character_in_word == five_character_word[3]:
        print(single_character_in_word + " found at index 3")
        count_for_instances_of_similarity = count_for_instances_of_similarity + 1
    if single_character_in_word == five_character_word[4]:
        print(single_character_in_word + " found at index 4")
        count_for_instances_of_similarity = count_for_instances_of_similarity + 1
    

if count_for_instances_of_similarity == 1:                    
    print(str(count_for_instances_of_similarity) + " instance of " + single_character_in_word + " found in  " + five_character_word)
else:
    if count_for_instances_of_similarity >= 2:
        print(str(count_for_instances_of_similarity) + " instances of " + single_character_in_word + " found in  " + five_character_word)
    else:
        print(" No instances of " + single_character_in_word + " found in  " + five_character_word)
