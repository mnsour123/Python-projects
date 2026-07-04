import random


def play_game():
    LOW = 1
    HIGH = 100
    secret_number = random.randint(LOW, HIGH)

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {LOW} and {HIGH}.")
    print("Try to guess it!")

    guess = None
    attempts = 0

    while guess != secret_number:
        user_input = input(f"Enter your guess ({LOW}-{HIGH}): ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if guess < LOW or guess > HIGH:
            print(f"Your guess must be between {LOW} and {HIGH}.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")


if __name__ == "__main__":
    play_game()
