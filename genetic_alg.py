import string
import random

possibleCharacters = string.ascii_letters + string.digits + " ,.:;-?!'\""

with open('lotr.txt', 'r') as file:
    t = file.read().strip()

def generate_string(target):
    length = len(target)
    randomtest = ''.join(random.choice(possibleCharacters) for _ in range(length))
    return randomtest

def fitness(curAttempt):
    return sum(1 for a, b in zip(curAttempt, t) if a == b)

def mutate(parent):
    index = random.randint(0, len(parent) - 1)
    child = list(parent)
    child[index] = random.choice(possibleCharacters)
    return ''.join(child)

attempt = generate_string(t)
iteration = 0

while attempt != t:
    print(attempt)
    new = mutate(attempt)
    if fitness(new) >= fitness(attempt):
        attempt = new
    iteration += 1
print(attempt)
print(f"Target reached: {iteration} iterations.")
