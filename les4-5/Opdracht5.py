def swap(lijst):
    returnLijst = lijst.copy()
    eerste = returnLijst[0]
    returnLijst[0] = returnLijst[-1]
    returnLijst[-1] = eerste
    return returnLijst

def shift(lijst):
    returnLijst = lijst.copy()
    laatste = returnLijst[-1]
    returnLijst.pop(-1)
    returnLijst.insert(0, laatste)
    return returnLijst

def replaceEvenWithZeros(lijst):
    returnLijst = lijst.copy()
    for i in range(len(returnLijst)):
        if returnLijst[i] % 2 == 0:
            returnLijst[i] = 0
    return returnLijst

def moveEvenToFront(lijst):
    dummy = []
    index = 0
    for i in range(len(lijst)):
        if lijst[i] % 2 == 0:
            dummy.insert(index, lijst[i])
            index += 1
        else:
            dummy += [lijst[i]]
    return dummy

def reverse(lijst):
    returnLijst = lijst.copy()
    returnLijst = returnLijst[::-1]
    return returnLijst

def main():
    lijstVB = [9, 2, 5, 5, 3, 1, 2, 4, 3, 2, 2, 2, 2, 3, 6, 5, 5, 6, 3, 1]
    print(swap(lijstVB))
    print(shift(lijstVB))
    print(replaceEvenWithZeros(lijstVB))
    print(lijstVB)
    print(moveEvenToFront(lijstVB))
    print(reverse(lijstVB))

main()