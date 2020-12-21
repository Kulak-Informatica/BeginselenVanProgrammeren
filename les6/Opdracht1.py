def zoekKleinste(lijst, ind):
    if (ind == 1):
        return lijst[0]
    return min(lijst[ind-1], zoekKleinste(lijst, ind-1))



def main():
    lijst = [80, 10, 55, 874, 123, 1564867, 121, 45657, 12, 354, 564, 68, 46]
    a = len(lijst)
    min = zoekKleinste(lijst, a)
    print(min)

main()