num = float(input("Float: "))

if num == 0:
    print("Dit getal is nul.")
else:
    text = ""

    # test the size
    if abs(num) > 100000:
        text += "groot "
    elif abs(num) < 1:
        text += "klein "

    # test the sign
    if num > 0:
        text += "positief"
    else:
        text += "negatief"
    print(f"Dit is een {text} getal")
