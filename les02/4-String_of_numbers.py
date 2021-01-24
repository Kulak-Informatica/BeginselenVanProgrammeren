numbers = input("Enter a string of numbers, use space \" \" between them and end with 0.\n> ")

lnumbs = numbers.split(" ")
total = 0
i = 0

for current in lnumbs:
    current = int(current)
    if not current:  # "if 0"
        break
    elif not i % 2:  # "is not even"
        total += current
    else:
        total -= current

print(total)
