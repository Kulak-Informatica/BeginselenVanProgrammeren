def all_same(items):
    return all(x == items[0] for x in items)

def checkHor(matrix):
    somLijst = []
    for i in range(4):
        som = 0
        for j in range(4):
            som += matrix[i][j]
        somLijst += [som]
    if all_same(somLijst):
        return True, somLijst[0]
    return False, somLijst[0]

def checkVer(matrix):
    somLijst = []

    for i in range(4):
        som = 0
        for j in range(4):
            som += matrix[j][i]
        somLijst += [som]

    if all_same(somLijst):
        return True, somLijst[0]
    return False, somLijst[0]

def checkDiags(matrix):
    som = 0
    som1 = 0
    for i in range(4):
        som += matrix[i][i]
        som1 += matrix[::-1][i][i]
    if som == som1:
        return True, som
    return False, som



def main():
    matrix = []
    for i in range(4):
        string = input("").split(" ")
        lijn = []
        for j in string:
            lijn += [int(j)]
        matrix += [lijn]

    returned, returned1, returned2 = checkHor(matrix), checkVer(matrix), checkDiags(matrix)
    if returned[0] and returned1[0] and returned2[0]:
        som, som1, som2 = returned[1], returned1[1], returned2[1]
        if som == som1 and som1 == som2:
            print("Magic")
        else:
            print("No Magic")
    else:
        print("No Magic")
main()


"""
1 15 14 4
10 11 8 5
7 6 9 12
16 2 3 13

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""