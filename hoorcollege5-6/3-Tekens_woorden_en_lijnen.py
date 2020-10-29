# als input is het onmogelijk om newlines te creëren.
# Dus: we definiëren een functie in de plaats:

def wordcount(text):
    text = text.replace("\n", " ")

    words = text.split(" ")
    for word in list(words):
        if word == "":
            words.remove(word)

    return len(words)  # returns length of list


def charcount(text):
    return len(text)  # returns length of string


def linecount(text):
    return len(text.split("\n"))  # returns length of list


def wc(text):  # hehe funny word wc LOL
    return linecount(text), wordcount(text), charcount(text)


# Test value:
txt = "Hello! I am David. This is my pet named Steve; he loves my humungous, enormously large\n"  # 87 chars
txt += "cookie dispenser, because he loves cookies too.\n"  # 48 chars
txt += "You were thinking something entirely different, weren't you?\n"  # 61 chars
txt += "Oh my how lewd. aheuheahiauhauauheuahaha..."  # 43 chars => 239 chars total
print(wc(txt))  # 4 lines, 36 words, 239 chars AND IT WORRRKKKSS First tryy, hell yeeaaaa
