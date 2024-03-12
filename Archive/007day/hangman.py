import random
import hangman_art
import hangman_words


print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

lives = 6

# Create blanks
display = []
for ch in chosen_word:
    display.append("_")

end_game = False

# Check guessed letter
while not end_game:
    guess = input("Guess a letter: ").lower()

    # Clear screen
    print('\x1b[2J')

    if guess in display:
        print(f"You've already gueesed {guess}")
    
    for pos in range(len(chosen_word)):
        if chosen_word[pos] == guess:
            display[pos] = guess                    
   
    if (guess not in chosen_word):
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You loose a life.")
        if lives == 0:
            end_game = True
            print("You loose!")
            
    print(f"{' '.join(display)}")

    if ("_" not in display) and (lives > 0):
        end_game = True
        print("You win!")
    
    print(hangman_art.stages[lives])

