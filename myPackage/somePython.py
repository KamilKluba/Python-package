import string


def caesar(plaintext):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[1:] + alphabet[:1]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)
