"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730772599"


def input_word() -> str:
    """Checks if the word is 5 characters long"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:  # checks if input is not 5 characters long
        print(
            "Error: Word must contain 5 characters."
        )  # notifies user that their input isn't 5 characters long
        exit()  # exits program so it doesn't return the invalid word
    return word  # returns word if the input is 5 characters long


def input_letter() -> str:
    """Checks if the letter is 1 character long"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:  # checks if input is not 1 character long
        print(
            "Error: Character must be a single character."
        )  # notifies user that their input isn't 1 character long
        exit()  # exits program so it doesn't return the invalid letter
    return letter  # returns letter if the input is 1 character long


def contains_char(word: str, letter: str) -> None:
    """Checks if word contains the letter and displays number of letter's instances"""
    count: int = 0  # defines counter variable
    print("Searching for " + letter + " in " + word)

    # iterates through each letter of the word to check if it's the inputted letter
    for i in range(len(word)):
        if word[i] == letter:
            print(letter + " found at index " + str(i))
            count += 1  # increments counter for each iteration

    if count == 0:
        print(
            "No instances of " + letter + " found in " + word
        )  # custom message for no instances of the letter
    elif count == 1:
        print(
            "1 instance of " + letter + " found in " + word
        )  # custom message for 1 instance of the letter
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # reports number of instances of the letter


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
