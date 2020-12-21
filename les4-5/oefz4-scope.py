# Scope oefening


def berekenLeeftijdInDagen(leeftijdInJaar):
    dagenPerJaar = 365
    leeftijdInDagen = leeftijdInJaar*dagenPerJaar
    return leeftijdInDagen


def berekenLeeftijdInMaanden(leeftijd):
    resultaat = leeftijd*maandenPerJaar
    return resultaat


def main():
    global maandenPerJaar
    maandenPerJaar = 12
    leeftijd = 23
    leeftijdInMaanden = berekenLeeftijdInMaanden(leeftijd)
    leeftijdInDagen = berekenLeeftijdInDagen(leeftijd)
    
    print("leeftijd in maanden: ", leeftijdInMaanden, 
    " en leeftijd in dagen: ", leeftijdInDagen)
    
    
main()
