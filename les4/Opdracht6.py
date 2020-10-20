import string

def cleanWord(w):
    return w.lower().strip(string.punctuation)

def getWoorden(zin, geheugen):
    zin = zin.split(" ")
    newSet = set()
    for i in zin:
        woord = cleanWord(i)
        if woord not in list(geheugen.keys()):
            geheugen[woord] = 1
            newSet.add(woord)
        else:
            geheugen[woord] += 1

    return geheugen, newSet


def main():
    zin = input("Verwerkte zin: ")
    geheugen = dict()

    amount = 0
    while zin != "KLAAR":
        laatsteZin = zin.split(" ")

        functie = getWoorden(zin, geheugen)
        geheugen = functie[0]
        nieuweWoorden = functie[1]

        print(f"Grootte van de nieuwe woordenschat: {len(list(geheugen.keys()))}")
        print(f"Nieuwe woorden toegevoegd: {nieuweWoorden}")
        zin = input("Verwerkte zin: ")
        amount += 1

    for i in range(len(laatsteZin)):
        laatsteZin[i] = cleanWord(laatsteZin[i])

    string = ""
    for i in laatsteZin:
        if geheugen[i]/amount > 0.5:
            string += f"{i} "

    print(f"Woorden die in meer dan 50% van de zinnen voorkomen: {string}")
main()