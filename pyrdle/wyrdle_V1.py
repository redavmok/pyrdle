import pathlib
import random 

WORDLIST = pathlib.Path("wordlist.txt")

## insert a file cleaner block here

## change this block to not use a pathlib
words = [
    word.upper()
    for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
]
# this records all guessed words
almanac = list()
WORD = random.choice(words)
count_total = 0

print(WORD)


for guess_num in range(1,7):
    guess = input(f"\n{guess_num}:").upper()
    if len(guess) != 5:
        print("Error! Not 5 letters long!")
        continue
    else:
        almanac.append(guess)
        if guess == WORD:
            print("Correct")
            break
        else:
             print("Wrong")

        # create a scoring algorithim with these blocks
        correct_letters = {letter for letter, correct in zip(guess, WORD) if letter == correct}
        misplaced_letters = set(guess) & set(WORD) - correct_letters
        wrong_letters = set(guess) - set(WORD)

        count_correct_letters = len(correct_letters) * 2
        count_misplaced_letters = len(misplaced_letters)
        count_total = count_total + count_correct_letters + count_misplaced_letters

    print("Correct letters:", ", ".join((correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

## insert a graphical representation of the word being guessed here

else:
    print(f"The word was {WORD}, you guessed {almanac}.")
print(f"Total score for this game was",count_total)