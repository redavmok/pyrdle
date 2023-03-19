# Pyrdle

Pyrdle is a command line clone of the popular word guessing game Wordle, designed for Assessment 2 of Unit ICTPRG302.

## Description

Pyrdle gives the player 6 chances to guess a five letter word. After 6 chances, or when the player guesses a word correctly, the program will award a score out of 100 to indicate how 'well' the game was played.

Pyrdle takes into consideration multiple of the same letter appearing, duplicate words, improper guess length and can read any word list put through to it (well, almost).
Pyrdle is open source to ensure complete security and transparancy of under the hood.

## Getting Started

### Dependencies

* Windows 10
* Python3 
* Terminal

### Installing

* Download and save the program file to your desktop

### Executing program

* Run the below code in the below terminal to initiate the game
```
python3 pyrdle.py
```

## Help

I probably don't know the answer to the question yet!

## Version History

* Version 1
    * First working version of the program that could be played start to finish.

* Version 2
    * Updated code to be more efficient and utilise functions.
    * Removed need for pathlib dependency.
    * Implemented the ability for any file to be used as the word list (program will still only use 5-letter words however).
    * Added a visual representation of each guess & wrong/misplaced/correct letters
* Version 3
    * XXX

* Version 3
    * 


## License

This project is licensed under the Unlicense License - see the LICENSE.md file for details

## Acknowledgments

* [wordle official site](https://www.nytimes.com/games/wordle/index.html)
