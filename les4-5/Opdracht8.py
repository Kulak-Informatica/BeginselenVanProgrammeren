def coderen(l1, l2, TF):
    geheugen = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "lst", "t", "u",
                "v", "w", "x", "y", "z"]
    if l1 not in geheugen:
        return l1


    getal1 = geheugen.index(l1.lower())
    getal2 = geheugen.index(l2.lower())

    if TF:
        returnedGetal = getal1 + getal2
        if returnedGetal > len(geheugen):
            returnedGetal -= len(geheugen)
    else:
        returnedGetal = getal1 - getal2
        if returnedGetal > len(geheugen):
            returnedGetal += len(geheugen)

    if l1.islower():
        return geheugen[returnedGetal]
    return geheugen[returnedGetal].upper()

def main():
    coderenTF = input("Coderen? (j/n) \n> ")
    if coderenTF == "j":
        coderenTF = True
    else: coderenTF = False

    string = input("> ")
    word = input("> ")
    for i in range(len(string)):
        print(coderen(string[i], word[i], coderenTF), end="")

main()