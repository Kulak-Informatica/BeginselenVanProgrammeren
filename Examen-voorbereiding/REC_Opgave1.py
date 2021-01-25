def weeg(blokjes_a, blokjes_b):
    global blokjes_verz  # Checklist van welk blok werkelijk de ster heeft

    # Check of er meer blokjes zitten in een bepaalde lijst
    if len(blokjes_a) > len(blokjes_b):
        return -1
    elif len(blokjes_a) < len(blokjes_b):
        return 1

    # - De lijsten zijn even lang: gewicht wordt bepaald door het blok met de ster.

    # Check of het zwaarder blok in a zit:
    for blokID in blokjes_a:
        if blokjes_verz[blokID]:
            return -1
    # Check of het zwaarder blok in b zit
    for blokID in blokjes_b:
        if blokjes_verz[blokID]:
            return 1

    # Geen van beide lijsten heeft een zwaarder blok => wegen evenveel
    return 0


def vind_ster_recursief(bloklijst):
    # -- Als de lengte 1 of 0 is, is er iets misgegaan: raise een Error:
    if len(bloklijst) < 2:
        raise ValueError("De bloklijst heeft minder dan 2 blokken, blokken vergelijken is niet mogelijk")

    # Recursie heeft altijd een base case, die het meest simpele antwoord geeft. Dit is altijd de laatste stap bij
    # recursie. Hier geeft dit dus het blok met de ster weer.

    # -- Base case: lengte van de lijst is 2 => Check of het ene blok zwaarder is
    if len(bloklijst) == 2:
        zwaarste_blok = weeg([bloklijst[0]], [bloklijst[1]])  # weeg(a, b) verwacht lijsten, vandaar de extra []
        if zwaarste_blok == -1:
            return bloklijst[0]
        elif zwaarste_blok == 0:
            return -1  # het blok met de ster zit er niet in.
        else:
            return bloklijst[1]

    # -- Recursion:
    # Twee mogelijkheden: de bloklijst heeft een even lengte of de bloklijst heeft een oneven lengte.
    # - Mogelijkheid 1: Even lengte
    # Splits in twee en check welkeen het zwaarst is
    if not len(bloklijst) % 2:
        midden = len(bloklijst) // 2  # stel len == 4, dan is midden == 2, en dan "slicen" we naar "[0, 1]" en "[2, 3]"
        bloklijst_a = bloklijst[:midden]  # begin tot midden
        bloklijst_b = bloklijst[midden:]  # midden t.e.m. einde

        zwaarst = weeg(bloklijst_a, bloklijst_b)
        if zwaarst == -1:
            # bloklijst_a is zwaarder, dus voeren we de functie uit op a:
            return vind_ster_recursief(bloklijst_a)
        elif zwaarst == 0:
            # beiden even zwaar: geen info, return -1
            return -1
        else:
            return vind_ster_recursief(bloklijst_b)

    # - Mogelijkheid 2: Oneven lengte
    # Haal het laatste element uit de lijst en weeg dan een lijst met even elementen in.
    # Als de lijst het blok met ster niet heeft, returnt het -1. dwz dat het het uitgehaalde blok (mogelijks) de ster
    # bevat. Weeg dat laatste blok dan met een willekeurig (of eerste) blok om te checken.
    laatste_blok = bloklijst.pop(-1)  # list.pop verwijdert en returnt het opgegeven element.
    blok_met_ster = vind_ster_recursief(bloklijst)
    if blok_met_ster == -1:
        zwaarst = weeg([bloklijst[0]], [laatste_blok])
        if zwaarst == 1:
            return laatste_blok
        else:
            return -1

    # De gevonden "blok met ster" is niet -1, dus is dit het blokID van de blok met de ster. return het.
    return blok_met_ster


def main():
    global blokjes_verz
    bloklijst = list(blokjes_verz)
    print(vind_ster_recursief(bloklijst))


blokjes_verz = {0: 0, 1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}  # als value == 1: blok heeft ster
main()
