f = float(input("> "))

mess = "Dit getal is "

if f == 0:
    mess += "0"
else:
    mess += "een "

    if abs(f) < 1:
        mess += "klein "
    elif abs(f) > 1000000:
        mess += "groot "

    if f < 0:
        mess += "negatief getal"
    else:
        mess += "positief getal"

print(mess)