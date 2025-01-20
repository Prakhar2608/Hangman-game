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
Example of the game:
bash
Copy
_ _ _ _ _
Guess a letter: e
_ _ e _ _
Guess a letter: a
_ _ e _ _
Guess a letter: t
t _ e _ _
Guess a letter: r
t _ e r _
Guess a letter: p
t _ e r p
You win!
Game Over Example:
bash
Copy
_ _ _ _ _
Guess a letter: z
_ _ _ _ _
Guess a letter: q
_ _ _ _ _
Guess a letter: y
_ _ _ _ _
Guess a letter: m
_ _ _ _ _
Guess a letter: b
_ _ _ _ _
You lose
Code Explanation:
Word Selection: The chosen_word is selected randomly from the world_list.
Game Loop: The game runs in a loop where the player can guess one letter at a time.
Word Display: The word is displayed with underscores for the unguessed letters and the correctly guessed ones in place.
Incorrect Guess: If the guess is incorrect, a life is lost and the hangman image corresponding to the number of incorrect guesses is displayed.
Game End Condition: The game ends either when all letters are guessed or when the player loses all their lives.
Customization:
You can modify the world_list in the wods file to include any words you want.
You can customize the stages in the art file to change the visual appearance of the hangman.