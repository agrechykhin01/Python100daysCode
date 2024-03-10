# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks

display = []
for ch in chosen_word:
    display.append("_")

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

win = False

# Check guessed letter

while not win:
    guess = input("Guess a letter: ").lower()
    
    for pos in range(len(chosen_word)):
        if chosen_word[pos] == guess:
            display[pos] = guess
             
    print(display)

    if "_" not in display:
        win = True

print("You win!")
