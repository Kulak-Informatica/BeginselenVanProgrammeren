def berekenAankoopHoeveelheid(tabel1, tabel2):
    aankopen = {}

    for groente, _, _ in tabel1:
        # Groente -> (aantal, prijs)
        aankopen[groente] = (0, 0)


    for gevraagdeGroente, benodigdAantal, minimumPrijs in tabel1:
        for beschikbareGroente, beschikbaarAantal, gevraagdePrijs in tabel2:

            if beschikbareGroente == gevraagdeGroente and gevraagdePrijs < (minimumPrijs * 1.1):
                aantalGekocht = min(benodigdAantal, beschikbaarAantal)

                aankopen[gevraagdeGroente] = (aantalGekocht, aantalGekocht * gevraagdePrijs)
                break

    return aankopen






# enkel gedefinieerd voor aantalDagen = [1,7]
def berekenMinimumPrijsNaAantalDagen(prijs, aantalDagen):
    if aantalDagen == 1:
        return prijs
    elif aantalDagen == 7:
        return float('inf')

    return (berekenMinimumPrijsNaAantalDagen(prijs, aantalDagen - 1) * 7) / (7 - (aantalDagen - 1))



def updateBenodigdheden(tabelBenodigdheden, tabelAankopen):
    resultaat = list(tabelBenodigdheden)

    # Ga door aankoop en pas benodigdheden aan (aantallen verminderen)
    for groente, (aantal, prijs) in tabelAankopen.items():

        for i in range(len(resultaat)):
            if resultaat[i][0] == groente:
                resultaat[i][1] -= aantal
                break

    return resultaat



def nieuweStrategie(tabellenStock, tabelBenodigdheden):

    aankopen = []
    huidigeTabelBenodigdHeden = list(tabelBenodigdheden)

    for dag, tabelStock in enumerate(tabellenStock):

        # Pas de minimumprijzen aan, a.d.h.v. de recursieve functie
        for i in range(len(tabelBenodigdheden)):
            huidigeTabelBenodigdHeden[i][2] = \
                berekenMinimumPrijsNaAantalDagen(tabelBenodigdheden[i][2], dag + 1)


        # Doe de aankopen
        aankoop = berekenAankoopHoeveelheid(huidigeTabelBenodigdHeden, tabelStock)

        # Pas de tabel met benodigdheden aan
        huidigeTabelBenodigdHeden = updateBenodigdheden(huidigeTabelBenodigdHeden, aankoop)

        # Hou de geschiedenis bij
        aankopen.append(aankoop)

    return aankopen







def main():
    tabel1 = [
        # Groente     Nodige eenheden  Geschatte min. prijs
        ['Bloemkool', 30,              10],
        ['Sla',       300,             7],
        ['Wortelen',  80,              8]
    ]

    tabel2 = [
        # Groente     Beschikbare eenheden  Prijs
        ['Bloemkool', 10,                   7],
        ['Wortelen',  800,                  18],
        ['Tomaten',   1000,                 1]
    ]

    print('Deel 1')
    aankoop = berekenAankoopHoeveelheid(tabel1, tabel2)
    print(f'\t{aankoop}')


    print('Deel 2')
    aankopen = nieuweStrategie([tabel2] * 7, tabel1)
    for aankoop in aankopen:
        print(f'\t{aankoop}')



if __name__ == '__main__':
    main()