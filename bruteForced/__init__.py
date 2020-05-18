from string import ascii_letters
from ceasarCipher import decrypted


def brute_force(str_input: str):
    alpha = ascii_letters
    alpha_length = len(alpha)

    brute_list = []
    for c in range(0, alpha_length):
        brute_list.append(decrypted.decrypt(str_input, c))

    return brute_list
