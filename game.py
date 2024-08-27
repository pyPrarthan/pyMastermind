# Importing random for generating random code
import random
from re import L

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

# Generate a random code of length CODE_LENGTH using random.choice
def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code 


# Function for the user to guess the code. 
def guess():

    while True:
        guess = input("Guess: ").upper().split()

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color{color}: Please use one of the following colors: {COLORS}")
                break
            else:
                return guess
        

print(guess())