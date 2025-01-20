import random
from wods import world_list
from art import stages
lives = 0
chosen_word = random.choice(world_list)
print(chosen_word)

empty_string = ""
for i in chosen_word:
    empty_string +="_"
print(empty_string)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()


    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    print(display)
    if guess not in chosen_word:
        lives +=1
        if lives == 6:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You win")
    print(stages[lives])