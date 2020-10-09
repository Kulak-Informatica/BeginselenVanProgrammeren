var = input("> ")
typeVar = "Letter"
nummer = 0
letter = ""
#17,14,11,8

for i in range(21):
    if str(i) == var:
        typeVar = "Getal"
        var = int(var)

if typeVar == "Letter":
    if "+" in var:
        nummer += 1
    elif "-" in var:
        nummer -= 1

    if "A" in var:
        nummer += 17
    elif "B" in var:
        nummer += 14
    elif "c" in var:
        nummer += 11
    else:
        nummer += 8

    print(f"Score: {nummer} / 20")

else:
    if var >= 16:
        letter += "A"
        if var > 17:
            letter += "+"
        elif var == 16:
            letter += "-"

    elif var >= 13:
        letter += "B"
        if var == 15:
            letter += "+"
        elif var == 13:
            letter += "-"

    elif var >= 10:
        letter += "C"
        if var == 12:
            letter += "+"
        elif var == 10:
            letter += "-"

    elif var >= 8:
        letter += "D"
        if var == 9:
            letter += "+"
    else:
        letter += "D-"

    print(f"Score: {letter}")