from words import words
import random
from string import ascii_lowercase
import os

list_of_words = words.split()
# print(list_of_words)
random_word = random.choice(list_of_words).lower()

alphabet = [x for x in ascii_lowercase]

def game():
    guessed_letters = set()
    lives = 10
    guessed = False
    while lives > 0 and not guessed:
        print('\n')
        os.system('cls')
        print("lives :", lives)
        guessed_letter = input("> ").lower()
        if guessed_letter not in alphabet:
            print("Enter a letter\n")
            continue
        if guessed_letter in guessed_letters:
            print("You already guessed this one !!\n")
            continue
        lives -= 1
        guessed_letters.add(guessed_letter)
        word_list = ['-' if letter not in guessed_letters else letter for letter in random_word]
        if '-' not in word_list:
            guessed = True
        print(" ".join(word_list))
        print()

    print(random_word)
    if guessed:
        print("You Win")
    else:
        print("You Lose")

if __name__ == '__main__':
    while True:
        game()
        ta = input("Wanna Play Again ? Y/N").lower()
        if ta == 'y':
            continue
        else :
            print("Good bye")
            break
