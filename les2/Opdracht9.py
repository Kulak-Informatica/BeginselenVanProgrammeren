def check(lst):
    som = 0
    for i in range(len(lst)):
        if (i % 2 == 0):
            getal = str(int(lst[i]) * 2)
            if len(getal) > 1:
                getal = int(getal[0]) + int(getal[1])
            lst[i] = int(getal)
            som += int(getal)

        else:
            som += int(lst[i])

    if som % 10 == 0:
        return True
    else:
        return False



invoer = input("> ")

lst = []
for i in invoer:
    lst += [int(i)]

numlst = []
cc = lst[15]
for i in range(10):
    if i != cc:
        numlst += [i]

if not check(lst):
    print("Niet geldig!")
    for i in numlst:
        lst[15] = i
        if check(lst):
            print(f"Ander controle getal: {i}")
            break
else:
    print("Geldig")






