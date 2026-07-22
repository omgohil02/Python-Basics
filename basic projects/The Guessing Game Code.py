# Guessing Game in Python

import random  # This gives us access to random number tools

print("Guess the Number Game")
print("I'm thinking of a number between 1 and 20.")

# 1. The computer picks a secret number
secret_number = random.randint(1, 20)  #generate a random number between 1 and 20
attempts = 0
guess = 0

# 2. Loop keeps running as long as the guess is wrong
while guess != secret_number:
    guess = int(input("Take a guess: "))
    attempts += 1  # Track how many turns you've taken

    # 3. Give feedback
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You found it in {attempts} attempts.")