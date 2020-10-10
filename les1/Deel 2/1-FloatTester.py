num = float(input("Float: "))

if num == 0:
    print("Dit getal is nul.")
else:
    size = ""
    charge= ""
    if abs(num) > 100000:
        size = "groot "
    elif abs(num) < 1:
        size = "klein "
    if num > 0:
        charge = "positief"
    else:
        charge = "negatief"
    print("Dit is een {}{} getal".format(size, charge))
