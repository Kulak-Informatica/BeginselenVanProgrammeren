# -*- coding: utf-8 -*-

# Bespreek hier kort (in enkele regels) je voornaamste moeilijkheden
"""
©   Karl Van Holder                     &   Thibaut Deliever
    Bachelor Ingenieurswetenschappen    &   Bachelor Informatica

Ter info: Onze source map heet 'Bestanden' en de map waar alle txt files komen, heet 'output'.
Deze dienen op voorhand aangemaakt te worden...

De opdracht is voor ons vlot verlopen, we hebben niet echt problemen ondervonden.
"""

# Functie die gegeven de locatie van een studentenlijst voor bedrijfsbezoeken naar iMinds, Barco en Bekaert
# een dictionary maakt met daarin voor elke student uit de lijst het bedrijf dat hij/zij zal bezoeken
def leesInformatieIn(studentenlijstFileLocatie, bedrijfFileLocatie):
    global bedrijfsbezoekenOverzicht

    """
    Openen van de files in 2 aparte lijsten, uitlezen en elke lijn als een apart item zien in een lijst door de 
    .split('\n') functie. Hierbij laten we het eerste element vallen aangezien dit toch de header is van de tabel. 
    Dit doen we door de functie '.pop(0)' te gebruiken, hierdoor valt het 0-ste element uit te lijst
    """
    studentenLijst = open(studentenlijstFileLocatie, 'r', encoding="utf8").read().split("\n")
    studentenLijst.pop(0)
    bedrijvenLijst = open(bedrijfFileLocatie, 'r', encoding="utf8").read().split("\n")
    bedrijvenLijst.pop(0)

    """
    Voordat we de dictionary kunnen opbouwen moeten we eerst ergens inlijsten welke reeks naar welk bedrijf kan gaan.
    Dit doen we door een aparte dictionary op te maken aan de hand van de variabele bedrijvenLijst. Op basis van reeksnr
    kunnen we het juiste bedrijf toekennen aan elke student. Omdat elke i in deze forlus 1 lange string is, splitsen we deze 
    per tab op in de variable 'lijn' om zo de dictionary op te maken. Aangezien 'reeks + nr' maximaal 7 tekens bevat kunnen we
    zo de keys bewaren voor de tempDict. Omdat het 2e item in 'lijn' een bedrijfsnaam is, is het vrij simpel om deze in te voegen
    in de dictionary. Ook is elke prof een key in deze verzameling waarbij de value per prof gelijk is aan de locatie waar
    ze naartoe gaan.
    """
    tempDict = dict()
    for i in bedrijvenLijst:
        lijn = i.split("\t")

        key = lijn[0][0:7]
        prof = lijn[0][9:-1]

        tempDict[key] = lijn[1]
        tempDict[prof] = lijn[1]

    """
    In deze forlus overloop ik de studentenlijst. Mijn variabele 'lijn' is een lijst van alle elementen van een regel 
    in de grote gehele studentenlijst. Hierbij splits ik elk element op de tab, waardoor ik nr, voornaam, achternaam,
    email en reeks kan opdelen van elkaar. Ik genereer enkele variabelen zoals naam die ik gebruik om mijn dictionary 
    op te bouwen. Ik kan dezelfde redenering volgen (voor de reeksbepaling) zoals hierboven. Zo kan ik uit mijn tempDict
    bepalen welke leerling naar welk bedrijf mag gaan. Dit werkt helaas niet voor de leerkrachten, hiervoor maak ik via een
    if-statement een uitzondering
    """
    for i in studentenLijst:
        lijn = i.split("\t")
        naamVn = f"{lijn[2]} {lijn[1]}"
        vnNaam = f"{lijn[1]} {lijn[2]}"

        if (lijn[4] == "Teaching Team") and (vnNaam in tempDict.keys()):    #prof die een locatie toegewezen heeft gekregen
            bedrijf = tempDict[vnNaam]
            bedrijfsbezoekenOverzicht[naamVn] = bedrijf

        elif (lijn[4] != "Teaching Team"):                                  #student
            reeksNr = lijn[4][0:7]
            bedrijf = tempDict[reeksNr]
            bedrijfsbezoekenOverzicht[naamVn] = bedrijf
    return None


# Gaat na of deelnemer met naam 'deelnemersnaam' op bezoek gaat naar
#   bedrijf met naam 'bedrijfsnaam' (volgens dictionary 'bedrijfsbezoekenOverzicht')
def isDeelnemerAanBezoek(deelnemersnaam, bedrijfsnaam):
    global bedrijfsbezoekenOverzicht

    """
    Met deze if zoeken we in de globale dictionary als de naam uberhaupt geregistreerd staat, zoja kunnen we pas checken
    naar waar deze persoon gaat en als dit overeenkomt met het gevraagde bedrijf.
    """
    if deelnemersnaam in bedrijfsbezoekenOverzicht.keys() and bedrijfsbezoekenOverzicht[deelnemersnaam] == bedrijfsnaam:
        return True
    return False


# Returnt een collectie die alle bezoekers voor bedrijf met naam 'bedrijfsnaam' bevat
def getBezoekersVoorBedrijf(bedrijfsnaam):
    global bedrijfsbezoekenOverzicht

    """
    returnList is een geïnitialiseerde lijst die ik invul met de volgende forlus. Deze overloopt elke key en value van de
    dictionary en controleert als de value overeenkomt met het gevraagde bedrijf. Indien dit zo is, voegt het de persoon
    in kwestie toe aan de lijst die wordt teruggegeven op het einde van de functie.
    """
    returnList = []
    for k, v in bedrijfsbezoekenOverzicht.items():
        if v == bedrijfsnaam:
            returnList += [k]

    return returnList


# Print een overzicht met per bedrijf alle bezoekers in alfabetische volgorde
def printBedrijfsbezoekOverzicht():
    global bedrijfsbezoekenOverzicht

    """
    Er zijn 3 bedrijven, deze worden weergegeven in onderstaande bedrijven-lijst. In de forlus overlopen we bedrijf per bedrijf
    waarbij we de lengte van de bedrijfsnamen opgeslagen hebben in de variabele 'spaties', de +2 komt van de ": " wat 2 
    tekens bevat. Dan vragen we via de functie die we alreeds geschreven hebben de lijst met studenten op voor het bedrijf in 
    kwestie. Doordat de return hiervan een lijst is, kunnen we dit eenvoudig sorteren aan de hand van de functie 'sorted()'.
    Dan volgt een print commando aan de hand van de lengte van de lijst met studenten.
    """
    bedrijven = []
    for i in bedrijfsbezoekenOverzicht.values():
        if i not in bedrijven:
            bedrijven += [i]
    bedrijven = sorted(bedrijven)

    for bedrijf in bedrijven:
        spaties = len(bedrijf) + 2
        studentenLijst = sorted(getBezoekersVoorBedrijf(bedrijf))

        print(f"{bedrijf}: ", end="")
        for i in range(len(studentenLijst)):
            if i == 0:
                print(studentenLijst[i])
            else:
                print(" "*(spaties), end="")
                print(f"{studentenLijst[i]}")

        print()     #Lege print om lege lijn te krijgen tussen elk bedrijf

    return None


def genereerDeelnemerslijsten():
    global bedrijfsbezoekenOverzicht
    locatie = "output/"

    """
    We genereren opnieuw een lijst van alle mogelijke bedrijven en slaan deze op in een lijst genaamd 'bedrijven'. Nadien
    bekijken we bedrijf per bedrijf wie dat de deelnemers zijn (gesorteerd op achternaam) en deze staan opgeslagen in de
    variabele 'deelnemersLijst'. Dan maken we een relatieve locatie op waar de file zich zou opslaan en maken we 1 lange string
    tekst op die wordt overgeschreven in de txt file.
    """

    bedrijven = []
    for i in bedrijfsbezoekenOverzicht.values():
        if i not in bedrijven:
            bedrijven += [i]

    for bedrijf in bedrijven:
        deelnemersLijst = sorted(getBezoekersVoorBedrijf(bedrijf))
        fileLocatie = f"{locatie}deelnemerslijst_{bedrijf}.txt"

        output = f"Deelnemerslijst voor het bedrijfsbezoek aan {bedrijf}:\n"
        for student in deelnemersLijst:
            output += f"{student}\n"

        with open(fileLocatie, "w+", encoding="utf8") as f:
            f.write(output)




def consoleApplicatie():
    boodschap = "1: Ga na of een student meegaat naar een bepaald bedrijf\n"
    boodschap += "2: Toon een overzicht van alle bezoekers voor een bepaald bedrijf\n"
    boodschap += "3: Toon een overzicht van alle bedrijfsbezoeken\n"
    boodschap += "4: Genereer .txt van deelnemers per bedrijf\n"
    boodschap += "0: sluit af\n"
    boodschap += "Invoer: "

    invoerGetal = int(input(boodschap))

    while invoerGetal != 0:
        if invoerGetal == 1:
            naam = input("Naam student: ")
            bedrijfsnaam = input("Naam bedrijf: ")
            print(isDeelnemerAanBezoek(naam, bedrijfsnaam))
            print()

        elif invoerGetal == 2:
            bedrijfsnaam = input("Naam bedrijf: ")
            print(getBezoekersVoorBedrijf(bedrijfsnaam))
            print()

        elif invoerGetal == 3:
            printBedrijfsbezoekOverzicht()

        elif invoerGetal == 4:
            genereerDeelnemerslijsten()
            print()
        else:
            print("Ongeldige invoer!")

        invoerGetal = int(input(boodschap))  # Nieuwe invoer inlezen


def main():
    global bedrijfsbezoekenOverzicht

    bedrijfsbezoekenOverzicht = {}  # Initieel: leeg dictionary

    studentenlijstFileLocatie = f"./Bestanden/Studenten2020-21.txt"  # pas dit aan naar de juiste locatie van de studentenlijst
    bedrijfFileLocatie = f"./Bestanden/bedrijven2020-21.txt"  # pas dit aan naar de juiste locatie van de bedrijvenlijst
    leesInformatieIn(studentenlijstFileLocatie, bedrijfFileLocatie)

    consoleApplicatie()

main()
