# -*- coding: utf-8 -*-
"""
Vereenvoudiging voor het weergeven van informatie over de geplande bedrijfsbezoeken
:author:    Dieter Demuynck
:date:      08-11-2020
:time:      01:05

It took me two hours, and I am not awake. I HAVE to be a masochist to be willing to do this... that's nice :)
Also, author and date and time here are not official ways to note these down. I don't actually know how. idc rn tho.
"""
# Bespreking voornaamste moeilijkheden
#
# - Het was in het begin onduidelijk of de variabele bedrijfsbezoekenOverzicht
#   de dictionary is die gevraagd is bij leesInformatieIn(). Ik ga ervan uit van wel. \
# - Bij printBedrijfsbezoekOverzicht() wordt er gevraagd van te printen, maar ook voor een return waarde. \
# - Uit gewoonte (en omdat ik dit deels schreef na 00:00) schrijf ik soms nog Engelse commentaar.


def leesInformatieIn(studentlist_location, companylist_location):
    """
    Functie die gegeven de locatie van een studentenlijst voor bedrijfsbezoeken naar iMinds, Barco en Bekaert
    een dictionary maakt met daarin voor elke student uit de lijst het bedrijf dat hij/zij zal bezoeken
    :param studentlist_location: Locatie van de lijst van studenten
    :param companylist_location: Locatie van de lijst van bedrijven
    :return: Geen. De variabele bedrijfsbezoekenOverzicht neemt deze taak over.
    """
    global bedrijfsbezoekenOverzicht

    # Leest de bedrijfslijst en maakt een dict aan voor reeksnummers
    # te kunnen vertalen naar respectievelijke bedrijfsnamen
    with open(companylist_location, "r", encoding="utf8") as companies:
        digit_to_company = dict()  # dictionary om een reeksnummer te vertalen naar een bedrijfnaam

        line = companies.readline()  # lees de eerste lijn
        while line != "":  # txt bestand lijkt te eindigen op een lege lijn
            info = line.split("\t")
            if "Reeks" in info[0]:  # bedrijven worden altijd een reeksnummer toegekend
                reeks_id = info[0][6]  # reeksnummer staat op 7de plaats (len("Reeks ") = 6)
                companyname = info[-1].strip("\n")  # mogelijks staat er nog een newline, verwijder deze uit de naam
                digit_to_company[reeks_id] = companyname

            line = companies.readline()  # lees volgende lijn

    companies.close()  # sluit het bestand om efficiënter te kunnen werken

    with open(studentlist_location, "r", encoding="utf8") as students:
        line = students.readline()

        while line != "":
            info = line.split("\t")
            if "Reeks" in info[-1]:  # Deelnemers worden altijd een reeksnummer toegekend
                studentname = info[2] + " " + info[1]  # achternaam + spatie + voornaam

                # info[-1][6] is de reeksID van de deelnemer. Dit staat voor een bedrijf.
                companyname = digit_to_company[info[-1][6]]

                # Voeg de deelnemer met het bezochte bedrijf toe aan de dictionary.
                bedrijfsbezoekenOverzicht[studentname] = companyname

            line = students.readline()

    students.close()

    return None


def isDeelnemerAanBezoek(studentname, companyname):
    """
    Gaat na of deelnemer met naam 'deelnemersnaam' op bezoek gaat naar
    bedrijf met naam 'bedrijfsnaam' (volgens dictionary 'bedrijfsbezoekenOverzicht')
    :param studentname: naam van de deelnemer
    :param companyname: naam van het bedrijf
    :return: True als de deelnemer het bedrijf bezoekt, anders False
    """
    if studentname in bedrijfsbezoekenOverzicht:  # Ander foutmelding bij verkeerde naam/invoer.
        if bedrijfsbezoekenOverzicht[studentname] == companyname:
            return True

    return False


def getBezoekersVoorBedrijf(companyname):
    """
    Returnt een collectie die alle bezoekers voor bedrijf met naam 'bedrijfsnaam' bevat
    :param companyname: naam van het bezochte bedrijf
    :return: set met de namen van alle bezoekers voor dat bedrijf
    """
    visitors = set()
    for visitor, company in bedrijfsbezoekenOverzicht.items():  # most likely inefficient. Too bad!
        if companyname == company:
            visitors.add(visitor)

    return visitors  # set met
  

def printBedrijfsbezoekOverzicht():
    """
    Print een overzicht met per bedrijf alle bezoekers in alfabetische volgorde
    :return: Geen, deze functie print alleen.
    """
    # Neem de values van de var hierboven, verwijder alle duplicates, maak er een gesorteerde list van
    companies = list(set(bedrijfsbezoekenOverzicht.values()))
    companies.sort()

    # voor elk bedrijf, print alle bezoekers, gesorteerd op naam
    for company in companies:
        # Neem alle bezoekers, maak van de set een list en sorteer ze (alfabetisch)
        visitors = list(getBezoekersVoorBedrijf(company))
        visitors.sort()

        # print per bezoeker het bedrijf dat ze bezoeken, en de naam van de bezoeker
        for visitor in visitors:
            print(f"{company:8s} --- {visitor}")  # Provides 8 Characters for company name

    return None  # I do believe this is supposed to be None? This function prints! It doesn't return anything!! ????
        

def consoleApplicatie():
    boodschap = "1: Ga na of een student meegaat naar een bepaald bedrijf\n"
    boodschap += "2: Toon een overzicht van alle bezoekers voor een bepaald bedrijf\n"
    boodschap += "3: Toon een overzicht van alle bedrijfsbezoeken\n"
    boodschap += "4: Genereer deelnemerslijsten per vedrijf als txt-bestanden in map Deelnemerslijsten/\n"
    boodschap += "0: sluit af\n> "
    
    invoerGetal = input(boodschap)  # needless int() removed, may cause errors if accidental string entered.
    
    while invoerGetal != "0":
        if invoerGetal == "1":
            # Case 1: Check if student goes to company or not
            studentname = input("Naam van de student\n> ")
            companyname = input("Naam van het bedrijf\n> ")
            if not isDeelnemerAanBezoek(studentname, companyname):
                going = "niet"
            else:
                going = "wel"

            # Vrij onduidelijk om te lezen in de console \/
            print(f"De student {studentname} gaat {going} mee naar het bedrijf {companyname}")
            print("=" * (39 + len(studentname) + len(going) + len(companyname)))  # ending line

            # Example output:
            # > Demuynck Dieter
            # > Barco
            # De student Demuynck Dieter gaat niet mee naar het bedrijf Barco
            # ===============================================================
            # (Nieuwe invoer)

        elif invoerGetal == "2":
            # Case 2: Show list of all visitors for a given company
            companyname = input("Naam van het bedrijf\n> ")

            print(f"\nAlle bezoekers voor het bedrijf {companyname}")
            print("-"*(32 + len(companyname)))  # seperation line

            # Example output:
            # > Barco
            # (\n)
            # Alle bezoekers voor het bedrijf Barco
            # -------------------------------------
            # visitor 1
            # visitor 2
            # visitor 3 ...
            visitors = list(getBezoekersVoorBedrijf(companyname))
            visitors.sort()
            for visitor in visitors:
                print(visitor)

            print("=" * (32 + len(companyname)))  # ending line
            # =====================================

        elif invoerGetal == "3":
            # Case 3: print all company visits
            printBedrijfsbezoekOverzicht()
            print("="*40)  # ending line
        elif invoerGetal == "4":
            genereerDeelnemerslijsten()
            print("Deelnemerslijsten gegenereerd.")
            print("="*40)  # ending line
        else:
            print("Ongeldige invoer!")
            
        invoerGetal = input(boodschap)


def genereerDeelnemerslijsten():
    """
        Print een overzicht met per bedrijf alle bezoekers in alfabetische volgorde
        :return: Geen, deze functie print alleen.
        """
    # Neem de values van de var hierboven, verwijder alle duplicates, maak er een gesorteerde list van
    companies = list(set(bedrijfsbezoekenOverzicht.values()))
    companies.sort()

    # voor elk bedrijf, print alle bezoekers, gesorteerd op naam
    for company in companies:
        company_file_name = "deelnemerslijst_" + company + ".txt"
        company_location = "Deelnemerslijsten/" + company_file_name

        visitors = list(getBezoekersVoorBedrijf(company))
        visitors.sort()

        with open(company_location, "w", encoding="utf8") as company_file:

            company_file.write("Deelnemerslijst voor het bedrijfsbezoek aan " + company + "\n")

            for visitor in visitors:
                company_file.write(visitor + "\n")

        company_file.close()

    return None


def main():
    global bedrijfsbezoekenOverzicht

    bedrijfsbezoekenOverzicht = {}

    studentenlijstFileLocatie = "studenten2020-21.txt"
    bedrijfFileLocatie = "bedrijven2020-21.txt"
    leesInformatieIn(studentenlijstFileLocatie, bedrijfFileLocatie)
    consoleApplicatie()

    
main()
