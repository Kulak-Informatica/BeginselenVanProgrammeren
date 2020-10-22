def getWoorden(line):
    from string import punctuation
    words = line.split()
    clean_words = set()
    for word in words:
        clean_words.add(word.lower().strip(punctuation))

    return clean_words


def leesBestand(name):
    with open(name) as file:
        text = file.read()
    file.close()

    return text.split("\n")


def main():
    filename = input("Name of file:\n> ")
    words = set()
    for line in leesBestand(filename):
        words.update(getWoorden(line))

    print(words)


main()
