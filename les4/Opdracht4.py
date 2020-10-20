import random

def getNum():
    return random.randint(1,6)

def checkList(lijst):
    voorgaande = lijst[0]
    tel = 0
    max = 0
    startPositie = 0
    for i in range(1, len(lijst)):
        if lijst[i] == voorgaande:
            tel += 1
        elif max < tel:
            max = tel
            startPositie = i - tel
            tel = 0
        else:
            tel = 0
        voorgaande = lijst[i]

    startPositie -= 1

    string = ""
    for i in range(len(lijst)):
        if i == startPositie:
            string += f"({lijst[i]} "
        elif i == startPositie+max:
            string += f"{lijst[i]}) "

        else:
            string += f"{lijst[i]} "

    return string

def main():
    lijst = []
    for i in range(20):
        lijst += [getNum()]

    #lijstVB = [1, 2, 5, 5, 3, 1, 2, 4, 3, 2, 2, 2, 2, 3, 6, 5, 5, 6, 3, 1]
    value = checkList(lijst)
    print(value)

main()