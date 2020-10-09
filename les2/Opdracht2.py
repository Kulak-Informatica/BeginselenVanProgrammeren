celsius = input("> ")

while celsius != "q":
    celsius = int(celsius)
    antwoord = int(1.8*celsius + 32)

    print(f"Antwoord: {antwoord}")
    print()
    celsius = input("> ")