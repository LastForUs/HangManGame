import random
import time
from words import words
import string
playing_again = True


def chose_a_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    global playing_again
    global try_again_teller
    try_again_teller = ''
    playing_again = False
    word = chose_a_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    guessed_letters = set()

    lives = 6
    left_lives = lives

    while len(word_letters) > 0:

        if left_lives <= 0:
            print("You Lost")
            time.sleep(0.5)
            print(f"The Word Was {word}")
            time.sleep(1.5)
            break
        print(f"You have {left_lives} more lives")
        print("You have used these letters", ' '.join(guessed_letters).upper())
        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print('Current Word Is:', ' '.join(word_list).upper())
        user_letter = input("Chose a letter >>").lower()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                left_lives -= 1

        elif user_letter in guessed_letters:
            print("You Have already Guessed it".title())
        else:
            print("WTF is that. Guess a word in the alphabet")
        if len(word_letters) <= 0:
            print("congratulations you win")


if playing_again:
    print("bug")
    hangman()


while True:
    print("Wanna Play Again")
    try_again_teller = input(">>")
    if try_again_teller == 'y':
        playing_again = True
        hangman()
    elif try_again_teller == 'n':
        break
    else:
        print("I didn't understand that")
