import random

print(" Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 50.")
print("You have 5 attempts to guess it.\n")

# Generate random number
secret_number = random.randint(1, 50)
attempts = 5

# Game loop
while attempts > 0:
    guess = input("Enter your guess: ")

    # Validate input
    if not guess.isdigit():
        print(" Please enter a valid number!")
        continue

    guess = int(guess)
    attempts -= 1

    if guess == secret_number:
        print(" Correct! You guessed the number!")
        break
    elif guess < secret_number:
        print(" Too low!")
    else:
        print(" Too high!")

    print(f"Attempts left: {attempts}\n")

# Game over
if attempts == 0:
    print(f"\n Game Over! The correct number was: {secret_number}")

print("\nThanks for playing! ")
