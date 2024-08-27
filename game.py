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
        

def check_code(guess, real_code):
    colors_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in colors_count: 
            colors_count[color] = 0
        colors_count[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_post += 1
            colors_count[guess_color] -= 1
        
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in colors_count and colors_count[guess_color] > 0:
            incorrect_pos += 1
            colors_count[guess_color] -= 1

    return correct_pos, incorrect_pos