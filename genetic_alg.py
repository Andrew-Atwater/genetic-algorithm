import string
import random

possibleCharacters = string.ascii_letters + string.ascii_digits + ' .,?!;:\'"'

t = "test"

def generate_string(target):
    length = len(target)
    possibleCharacters = string.ascii_letters + string.ascii_digits + ' .,?!;:\'"'
    random = ''.join(random.choice(possibleCharacters) for _ in range(length))
    return random

