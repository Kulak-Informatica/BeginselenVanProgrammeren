import time
##  Binair zoeken (recursief)
#   @param lijst: de lijst waarin gezocht wordt
#   @param getal: het te zoeken getal
#   @return: True als het getal in de lijst zit, anders False
#
def zoekBinair(lijst, getal):
    # Triviaal?
    if len(lijst) == 1:
        return getal == lijst[0]
    else:
        midden = len(lijst)//2  # bij even aantal elementen is dit de rechtse index!
        if getal < lijst[midden]:
            # Verder zoeken links
            return zoekBinair(lijst[:midden], getal)
        else:
            # Verder zoeken rechts (midden inclusief)
            return zoekBinair(lijst[midden:], getal)


# [1, 2, 3, 4], van=0, tot=4
def zoekBinair2(lijst, getal, van=0, tot=-1):
    if tot == -1:
        tot = len(lijst)

    # Triviaal?
    if van + 1 == tot:
        return getal == lijst[van]
    else:
        midden = (van + tot) // 2  # bij even aantal elementen is dit de rechtse index!
        if getal < lijst[midden]:
            # Verder zoeken links
            return zoekBinair2(lijst, getal, van, midden)
        else:
            # Verder zoeken rechts (midden inclusief)
            return zoekBinair2(lijst, getal, midden, tot)


def main():
    # Bereken de worst-case uitvoeringstijd voor binair zoeken:
    nrOfElem = 1000
    print("Test voor de initiële zoekBinair: ")
    for i in range(0, 20):
        # Maak problemen die telkens dubbel zo groot zijn als het vorige probleem
        langeLijst = [0]*nrOfElem*(2**i)  # Dit zijn allemaal nullen (dus gesorteerd)

        # en los het op
        startTime = time.perf_counter()
        zoekBinair2(langeLijst, 10)  # Zal nooit gevonden worden. Dus: recursie zal volledig doorlopen worden.
        endTime = time.perf_counter()

        timeTaken = endTime-startTime

        # print de probleemgrootte en de nodige tijd om het op te lossen
        print("Lijstlengte: %d \t: %f" % (len(langeLijst),timeTaken))

    print()
    print("Test voor de nieuwe verbeterde zoekBinair: ")
    print(" -> TODO")

main()