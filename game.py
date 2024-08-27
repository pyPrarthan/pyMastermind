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


code = generate_code()
print(code)