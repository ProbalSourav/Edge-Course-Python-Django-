import random

# Number of attempts allowed
max_attempts = 7
correct_number = random.randint(1, 100)  # Assume the number to be guessed

print("Welcome to the Number Guessing Game!")
print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")

for attempt in range(1, max_attempts + 1):
    guess = input(f"Attempt {attempt}: Enter your guess: ")

    # Check if the input is a digit (valid positive integer)
    if not guess.isdigit():
        print("Invalid input! Please enter a valid positive number.")
        continue  # Skip to the next attempt

    # Convert the guess to an integer
    guess = int(guess)

    # Check if the guess is within the valid range
    if guess < 1 or guess > 100:
        print("Your guess is out of range. Please guess a number between 1 and 100.")
        continue  # Skip to the next attempt

    # Compare the guess with the correct number
    if guess == correct_number:
        print(f"Congratulations! You guessed the correct number {correct_number} in {attempt} attempts.")
        break  # Exit the loop if the guess is correct
    elif guess < correct_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {correct_number}.")
