import random

guess = random.randint(1, 100)

print("Welcome to the guessing game.")
print("Guess the correct number between 1 and 100.")

print("You will have to keep on guessing till you get it right.")
while True:
    user_guess = int(input("Your guess: "))
    if user_guess < guess:
        print("Your guess is too low. \nTry again.")
    elif user_guess > guess:
        print("Your guess is too high.\nTry again.")
    elif user_guess == guess:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 100.")

print("Thanks for playing the game!")
