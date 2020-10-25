# I can already see people making fun of his name.
# Poor Virginère- I mean, Vigenère.

def main():
    text = input("Input string > ")
    codeword = input("Codeword > ")
    decode = input("Decode instead of code? [Y/N] > ").lower()

    if "y" in decode.lower():
        decode = -1
    else:
        decode = 1

    print(encode(text, codeword, decode))


def chartovar(string):
    key = []
    for char in string:
        key.append(ord(char) - 65)
    return key


def encode(text, codeword, step=1):
    # while codeword can fit in text: add entire code word + add the first part of the codeword that still fits
    # Hello I am David!
    # LEMONLEMONLEMONLE == "LEMON" * 3 + "LEMON"[0:2]
    # len(text) == 17 and len(key) == 5 => 17//5 == 3 FULL FITS and 17%5 == 2 EXTRA CHARACTERS
    key_string = codeword.upper() * (len(text) // len(codeword)) + codeword[0:len(text) % len(codeword)].upper()
    key = chartovar(key_string)  # list of the key for each character

    from string import ascii_uppercase, ascii_lowercase
    encrypted = ""
    for i in range(len(text)):
        char = text[i]
        if char in ascii_uppercase:
            encrypted += chr(((ord(char) - 65 + key[i] * step) % 26) + 65)  # probably should've made a function for this
        elif char in ascii_lowercase:
            encrypted += chr(((ord(char) - 97 + key[i] * step) % 26) + 97)
        else:
            encrypted += char
    return encrypted


main()
