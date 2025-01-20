Hangman Game
This is a Python implementation of the classic Hangman game. The game randomly selects a word from a predefined list, and the player has to guess the word by suggesting letters. Each incorrect guess results in a penalty (losing a life), and the game ends either when the player guesses the word or loses all their lives.

Features:
Random word selection from a list.
Player guesses a letter, and the program reveals all correct guesses.
The player loses a life for each incorrect guess.
The game ends when the player guesses the word correctly or exhausts all their lives.
Requirements:
Python 3.x

The wods and art modules (or files) must be available for the program to function properly.

wods: This file should contain the list of words (world_list) that the game will choose from.
art: This file should contain the stages for the hangman, which will be displayed during the game.
How to Run:
Ensure you have Python 3.x installed.
Make sure you have the wods and art files containing the necessary word list and hangman stages respectively.
Run the script.
bash
Copy
python hangman.py
Gameplay:
When the game starts, a random word is chosen from the word list, and the player is shown underscores (_) representing each letter in the word.
The player then guesses one letter at a time.
If the guessed letter is correct, it will be revealed in the word.
If the guessed letter is incorrect, the number of remaining lives decreases, and a part of the hangman is drawn on the screen.
The game continues until either the word is guessed or the player runs out of lives (6 wrong guesses).
The game displays a message indicating if the player won or lost and shows the final state of the hangman.
