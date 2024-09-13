def check_first_letter(word: str, letter: str):
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter("happy", "h"))
print(check_first_letter("happy", "s"))
