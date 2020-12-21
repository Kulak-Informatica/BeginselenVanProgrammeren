def pascal(n):
    if n == 0:
        return []

    elif n == 1:
        return [[1]]

    elif n == 2:
        return [[1], [1, 1]]

    else:
        rij = [1]
        driehoek = pascal(n-1)
        laatsteRij = driehoek[-1]
        for i in range(len(laatsteRij)-1):
            rij += [laatsteRij[i] + laatsteRij[i+1]]

        rij += [1]
        driehoek += [rij]

    return driehoek

def main():
    n = int(input("> "))
    lijst = pascal(n)
    for i in lijst:
        if len(i) != 1:
            for j in i:
                print(j, end="\t")
            print()
        else:
            print(i[0])

main()