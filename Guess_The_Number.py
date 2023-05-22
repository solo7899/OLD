#! python

import random

try:
    top = int(input("Pls Enter Top range : "))
except ValueError:
    print("You should enter numeric value.")
    quit()

if top <= 0:
    print("Number must be larger than 0.")
    quit()

r = random.randrange(0, top+1)

print(f"Guess a number between 0 and {top}")

try:
    tries = int(input("How many tries you need ? \n"))
except ValueError:
    print("Enter a Number !!")
    quit()

if tries <= 0: quit()

rounds = 0
guess = -1
guessed_nums = set()
while guess != r and tries > 0:
    print(f"You got {tries} tries left and have gone {rounds} rounds so far. ")
    try:
        guess = int(input("What is The number: "))
    except ValueError:
        print("Please Enter a Number!\n")
        continue

    if guess in guessed_nums:
        print("You've guessed this number before...\n")
        continue
    guessed_nums.add(guess)

    rounds += 1
    tries -= 1

    if guess > r:
        print("go lower\n")
    elif guess < r:
        print("go higher\n")

if guess == r:
    print("You win !!")
    print(f"you played {rounds} rounds to get the number. Good job :)")
else:
    print("You failed :(")
