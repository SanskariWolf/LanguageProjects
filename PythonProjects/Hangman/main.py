import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_word():
    words = ["hello","human","p ython"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def draw_hangman(attempts):
    hangman_graphics = [
        '''
           -----
           |   |
               |
               |
               |
               |
        ---------
        '''
        ,
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        '''
        ,
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        '''
        ,
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        '''
        ,
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        '''
        ,
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        '''
        ,
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        '''
    ]

    print(hangman_graphics[6 - attempts])

def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        clear_screen()
        print("Word: ", display_word(word_to_guess, guessed_letters))
        print("Guessed letters: ", guessed_letters)
        draw_hangman(attempts)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            input("Press Enter to continue...")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            input("Press Enter to continue...")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1

        if set(word_to_guess).issubset(guessed_letters):
            clear_screen()
            print("Congratulations! You guessed the word:", word_to_guess)
            break


    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    play_hangman()
