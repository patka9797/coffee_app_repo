import string

alphabet = string.ascii_lowercase


def caesar_cipher(string, step):
    outText = []
    cryptText = []
    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            crypt = (index + step) % 26
            cryptText.append(crypt)
            new_letter = alphabet[crypt]
            outText.append(new_letter)
    return outText


print(caesar_cipher("ko", 1))
