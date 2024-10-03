"""EX03 - Wordle in Python!"""

__author__ = "730772599"


def input_guess(word_length: int) -> str:
    """Prompts user and verifies if the user's guess is a valid length"""
    guess: str = input(f"Enter a {word_length} character word: ")

    # reprompts user for a guess until it's the right length
    while len(guess) != word_length:
        guess = input(f"That wasn't {word_length} chars! Try again: ")
    return guess


def contains_char(secret_word: str, guess_char: str) -> bool:
    """Searches through the secret word for an instance of the character input"""
    assert (
        len(guess_char) == 1
    )  # raises assertion error when the guess_char input is more than 1 char long
    idx: int = 0  # defines index counter variable

    # checks if the character is in the secret word
    while idx < len(secret_word):
        if secret_word[idx] == guess_char:
            return True
        idx += 1  # increments index counter per iteration
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Displays colored box emojis to show correctness of the guess"""
    assert len(guess) == len(
        secret_word
    )  # raises assertion error when the two inputs aren't the same length

    # unicode characters for colored box emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    idx: int = 0  # defines index counter variable
    result: str = ""  # defines empty string to add colored boxes in
    while idx < len(secret_word):
        if guess[idx] == secret_word[idx]:  # correct letter in correct position
            result += GREEN_BOX
        elif contains_char(
            secret_word, guess[idx]
        ):  # correct letter in incorrect position
            result += YELLOW_BOX
        else:  # letter does not exist in secret word
            result += WHITE_BOX
        idx += 1  # increments index counter per iteration
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 6  # hardcoded because instructions say "you have up to 6 turns"

    # state variables
    turn_number: int = 1
    won: bool = False

    while (
        turn_number <= turns and won == False
    ):  # checks if the user has remaining turns and hasn't won yet
        print(f"=== Turn {turn_number}/{turns} ===")
        guess: str = input_guess(
            len(secret)
        )  # stores guess in temporary variable so it can be used multiple times
        if len(guess) == len(
            secret
        ):  # added this if statement so it doesn't count an invalid guess as a turn
            print(emojified(guess, secret))
            if guess == secret:
                won = True
                print(f"You won in {turn_number}/{turns} turns!")
                exit()  # ends game so the losing message doesn't print
            turn_number += 1

    print(f"X/{turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
