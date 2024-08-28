__author__ = "730772599"


def mimic(message: str) -> str:
    """Says given message"""
    return message


def main() -> None:
    """Asks you for your message and prints the output of the mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
