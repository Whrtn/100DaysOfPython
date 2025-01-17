import random
from hangman_words import word_list
from hangman_art import hangman_ascii

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 0 or len(guess) > 1:
        print("Invalid guess, guesses should be 1 character!")
        print(f"You have guessed {guessed_letters}")
    elif guess in guessed_letters:
        print("This letter has already been guessed, try again!")
        print(f"You have guessed {guessed_letters}")
    else:
        display = ''
        guessed_letters.append(guess)
        for letter in chosen_word:
            if guess == letter:
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        if guess not in chosen_word:
            lives -= 1

        if "_" not in display:
            print("********************YOU WIN********************")
            game_over = True
            print(f"The word was {chosen_word}")
        elif lives == 0:
            print("********************YOU LOSE********************")
            print(hangman_ascii[lives])
            game_over = True
            print(f"The word was {chosen_word}")
        else:
            print(f"********************YOU HAVE {lives} LIVES LEFT********************")
            print(f"You have guessed {guessed_letters}")
            print(hangman_ascii[lives])
            print(display)

    


            

