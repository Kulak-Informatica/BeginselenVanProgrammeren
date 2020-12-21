def zoek(el, lijst):
    print(lijst)
    if (el != lijst[0] and len(lijst) == 1) or (lijst[0] > el):
        return False

    elif el != lijst[0]:
        lijst.pop(0)
        return zoek(el, lijst)

    else:
        return True

def main():
    lijst = [0, 1, 3, 4, 5, 8]
    print(zoek(2, lijst))

main()