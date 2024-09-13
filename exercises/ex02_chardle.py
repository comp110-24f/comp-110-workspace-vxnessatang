"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730772599"


def input_word() -> str:
    """Checks if the word is 5 characters long"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """Checks if the letter is 1 character long"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """Checks if word contains the letter and displays number of letter's instances"""
    count: int = 0
    print("Searching for " + letter + " in " + word)

    for i in range(len(word)):
        if word[i] == letter:
            print(letter + " found at index " + str(i))
            count += 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
