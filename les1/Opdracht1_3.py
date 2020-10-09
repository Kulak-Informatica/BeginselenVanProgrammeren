a = float(input("> "))
b = float(input("> "))
c = float(input("> "))

discr = (b**2) - (4*a*c)
if discr>0:
    w1 = (-b + (discr**0.5))/(2*a)
    w2 = (-b - (discr**0.5))/(2*a)
    print(f"Wortel 1: {w1}")
    print(f"Wortel 2: {w2}")

elif discr == 0:
    w = (-b)/(2*a)
    print(f"Wortel: {w}")

else:
    print("Er zijn geen reele wortels")