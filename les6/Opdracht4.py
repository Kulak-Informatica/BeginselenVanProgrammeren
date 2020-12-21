def som(lijst, n):
    if n == 1:
        return lijst[0]
    return lijst[n-1] + som(lijst, n-1)


def main():
    lijst = [int(x) for x in input("> ")]
    print(som(lijst, len(lijst)))

main()