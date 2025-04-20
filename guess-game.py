import random

guess = random.randint(1, 100)

print("Welcome to the guessing game.")
print("You have to guess the correct number between 1 and 100.")

print("You have 5 attempts to guess the correct number.")
attempts = 5
while attempts > 0:
    user_guess = int(input("Your guess: "))
    if user_guess < guess:
        print("Your guess is too low.")
    elif user_guess > guess:
        print("Your guess is too high.")
    elif user_guess == guess:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
    attempts -= 1
    if attempts == 1:
        print(f"You have {attempts} attempt left.")
    else:
        print(f"You have {attempts} attempts left.")

if attempts == 0:
    print("Sorry, you've used all your attempts. \nThe correct number was:", guess)
    print("Thanks for playing the game!")
