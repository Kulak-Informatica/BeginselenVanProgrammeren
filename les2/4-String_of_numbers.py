numbers = input("Enter a string of numbers, use space \" \" between them and end with 0.\n? ")

lnumbs = numbers.split(" ")
total = 0

for i in range(0, len(lnumbs)):
    current = int(lnumbs[i])
    if not current:
        break
    elif not i % 2:
        total += current
    else:
        total -= current

print(total)