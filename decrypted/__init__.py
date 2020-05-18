from ceasarCipher import encrypted


def decrypt(str_input: str, key: int):

    new_key = -key  # to decrypt a str, we had just put minus sign in the key
    str_decrypt = encrypted.encrypt(str_input, new_key)

    return str_decrypt
