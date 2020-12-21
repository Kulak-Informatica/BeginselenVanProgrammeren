## MergeSort: sorteert een lijst via mergesort
#   @param lijst: de te sorteren lijst
#   @return: een nieuwe lijst met de elementen van de gegeven lijst,
#            gesorteerd
#


def mergeSort(lijst):
    # Indien triviaal?
    if len(lijst) == 1:
        return lijst
    else:
        # splits op in twee
        midden = len(lijst)//2
        linkerhelft = lijst[:midden]
        rechterhelft = lijst[midden:]

        # sorteer recursief
        linksGesorteerd = mergeSort(linkerhelft)
        rechtsGesorteerd = mergeSort(rechterhelft)

        # en voeg samen...
        gesorteerd = []

        links, rechts = 0, 0

        while links < len(linksGesorteerd) and rechts < len(rechtsGesorteerd):
            if linksGesorteerd[links] < rechtsGesorteerd[rechts]:
                gesorteerd.append(linksGesorteerd[links])
                links += 1
            else:
                gesorteerd.append(rechtsGesorteerd[rechts])
                rechts += 1

        while rechts < len(rechtsGesorteerd):
                gesorteerd.append(rechtsGesorteerd[rechts])
                rechts += 1

        while links < len(linksGesorteerd):
                gesorteerd.append(linksGesorteerd[links])
                links += 1

        # en geef terug als resultaat
        return gesorteerd


def main():
    l = [10, 12, 7, 3, 15, 8, 9]
    print(mergeSort(l))


main()
