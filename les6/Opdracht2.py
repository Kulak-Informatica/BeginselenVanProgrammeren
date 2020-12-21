def average(lijst):
    n = len(lijst)
    if n == 1:
        return lijst[0]
    else:
        midden = n // 2
        return (midden * average(lijst[:midden]) + (n - midden) * average(lijst[midden:])) / n


def main():
    lijst = [80, 10, 55, 874, 123, 1564867, 121, 45657, 12, 354, 564, 68, 46]
    a = average(lijst)
    print(a)
    print(sum(lijst)/len(lijst))

main()