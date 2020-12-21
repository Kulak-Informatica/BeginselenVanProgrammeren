def checkPalindroom(lijst):
    if lijst[0] == lijst[-1] and len(lijst) > 2:
        lijst.pop(0)
        lijst.pop(-1)
        print(lijst)
        return checkPalindroom(lijst)

    if len(lijst) > 1 and lijst[0] != lijst[-1]:
        return False

    return True

def main():
    woord = input("> ").lower()
    lijst = list(woord)

    print(checkPalindroom(lijst))

main()
