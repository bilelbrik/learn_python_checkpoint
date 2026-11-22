import random


def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    # Generate a random integer between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None

    # Loop until the player guesses the correct number
    while guess != secret_number:
        # Prompt the player for their guess and convert it to an integer
        user_input = input("Enter your guess: ")
        guess = int(user_input)

        # Check if the guess is too high, too low, or correct
        if guess > secret_number:
            print("Your guess is too high. Guess again.")
        elif guess < secret_number:
            print("Your guess is too low. Guess again.")
        else:
            print("Congratulations! You guessed the number correctly!")


if __name__ == "__main__":
    guess_the_number()