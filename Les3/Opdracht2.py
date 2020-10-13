symbool = input("> ")
lijst = []
x = int(input("> "))

while x != 0:
    lijst += [x]
    x = int(input("> "))

max = max(lijst)
for i in lijst:
    perc = (i*100)//max
    print(symbool*int(((perc/100)*40)))