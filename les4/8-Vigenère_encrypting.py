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


def chartovar(string):
    code_seed = []
    for char in string:
        code_seed.append(ord(char) - 65)


def encode(text, codeword, i=1):
    # while codeword can fit in text: add entire code word + add the first part of the codeword that still fits
    # Hello I am David!
    # LEMONLEMONLEMONLE == "LEMON" * 3 + "LEMON"[0:2]
    # len(text) == 17 and len(key) == 5 => 17//5 == 3 FULL FITS and 17%5 == 2 EXTRA CHARACTERS
    key_string = codeword.upper() * (len(text) // len(codeword)) + codeword[0:len(text)%len(codeword)].upper()

