def fac(num):
    fac = 1
    for i in range(1, 1+num):
        fac*=i
    return fac


x = int(input("> "))
grens = float(input("> "))
n = 0

som = 0

var = x ** n
var = var / fac(n)

while var < grens:
    som += var
    n += 1

    var = x ** n
    var = var / fac(n)
    n += 1
