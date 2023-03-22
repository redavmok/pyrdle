    import (random word generator)

# this records all guessed words
    almanac = list()

# these track which letters are guessed, and whether in -guess- or not
    nope_list = (create list)
    yep_list = (create list)

# this sets the starting score
    start_score = 100

# word list generator
    file_name = input('Enter name of file: ')
    if length of file name = less than 1:
    print("No input, program stopped.")
    (stop program)
# opens and reads file
    text_file = open(file_name)
    text = text_file.read()
# cleans and strips the text
    words = text.words apart
    words = text.no invisible line indicators
    words = get rid of '.,!;()[]' in each word on each line
    words = replace ("'s") with a blank space in each word on each line
    word_list = all words uppercase

# this chooses the word to be guessed
    WORD = a random word from (word_list)

# dev tool to see the word
    print(WORD)


    def score_guess():
    """ score_guess counts each letter, and records whether they are a valid part of the word,
     then returns a score of the guess """

    count_misplaced_letters = len(missing_let)
    count_wrong_letters = len(wrong_let) * 2
    count_total = (count_misplaced_letters + count_wrong_letters)
    return count_total


# this is the core gameplay loop
    for guess_num in range(1, 7):
    guess = input(f"\n{guess_num}:").upper()
    correct_let = {letter for letter, correct in zip(guess, WORD) if letter == correct}
    missing_let = set(guess) & set(WORD) - correct_let
    wrong_let = set(guess) - set(WORD)
    if len(guess) != 5:
        print("Error! Not 5 letters long!")
        continue
    else:
# this block looks for whether the guess is correct, or whether it needs to be analysed
        almanac.append(guess)
        if guess == WORD:
            print("Correct!!")
            score -= score_guess()
            break
        else:
# this block creates a graphical representation of each guess
            print("Wrong.")
            for char, letter in zip(WORD, guess):
                if letter in WORD and letter in char:
                    print(letter + " ✔ ")

                elif letter in WORD:
                    print(letter + " + ")
                    if letter not in yep_list:
                        yep_list.append(letter)
                else:
                    print(" X ")
                    if letter not in nope_list:
                        nope_list.append(letter)
            print(f"Letters not in word: {nope_list}.")
            print(f"Letters that are in word: {yep_list}")

            score -= score_guess()

    print(f"The word was {WORD}, you guessed {almanac}!")
    print(f"Total score for this game was {score}/100!")