"""Checks if the user's guessed number matches the secret number"""

__author__ = "730772599"


def guess_a_number() -> None:
    """Checks the user's guessed number with the secret number"""
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))

    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
