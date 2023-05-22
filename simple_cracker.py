import os
import random
from string import ascii_lowercase, ascii_uppercase


nums = [str(x) for x in range(1, 10)]
lowers = [x for x in ascii_lowercase]
uppers = [x for x in ascii_uppercase]

chars = nums + lowers + uppers + [" ", ]

pwd = input("> ")
pw = ""

while pwd != pw:
    pw = ""
    for i in range(len(pwd)):
        pw += random.choice(chars)
    print(pw)
    os.system('cls')

print("your password is :", pw)
