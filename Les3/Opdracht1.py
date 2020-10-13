lijst = []

while len(lijst) < 10:
    x = int(input("> "))
    if x not in lijst:
        lijst += [x]

print(lijst)