numb = int(input("Insert a positive number: "))

fac = 1

if numb >= 2:
    for i in range(2, numb+1):
        fac *= i

print(fac)
