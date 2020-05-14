from string import ascii_letters  # import all letters of ascii code


def encrypt(str_input: str, key: int):
    alpha = ascii_letters

    result = ''

    for letter in str_input:  # for each letter in what user digit
        if letter not in alpha:  # if the character isn't in ascii code, the char don't change
            result += letter
        else:
            new_key = (alpha.index(letter) + key) % len(alpha)  # if the key is too large, this fix it
            result += alpha[new_key]

    return result
