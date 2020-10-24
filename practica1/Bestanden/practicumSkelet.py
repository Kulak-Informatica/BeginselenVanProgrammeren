# -*- coding: utf-8 -*-

#Bespreek hier kort (in enkele regels) je voornaamste moeilijkheden


#Functie die gegeven de locatie van een studentenlijst voor bedrijfsbezoeken naar iMinds, Barco en Bekaert
#een dictionary maakt met daarin voor elke student uit de lijst het bedrijf dat hij/zij zal bezoeken
def leesInformatieIn(studentenlijstFileLocatie, bedrijfFileLocatie):
    global bedrijfsbezoekenOverzicht #global keywoord nodig om de waarde van een globale variabele aan te passen in een functie
    

    #ToDo: Vul bedrijfsbezoekenOverzicht   
    #Merk op: deze functie zal geen terugkeerwaarde hebben! 
    #Doordat 'bedrijfsbezoekenOverzicht' als globale variabele gedefinieerd werd, kan je de inhoud
    #er van in elke andere functie opvragen.


    return None #return 'None' is equivalent met geen terugkeerwaarde hebben
    
    
#Gaat na of deelnemer met naam 'deelnemersnaam' op bezoek gaat naar 
#   bedrijf met naam 'bedrijfsnaam' (volgens dictionary 'bedrijfsbezoekenOverzicht')
def isDeelnemerAanBezoek(deelnemersnaam, bedrijfsnaam):
    #ToDo
    return None #Pas aan! Terugkeerwaarde is hier niet None


#Returnt een collectie die alle bezoekers voor bedrijf met naam 'bedrijfsnaam' bevat 
def getBezoekersVoorBedrijf(bedrijfsnaam):
    #ToDo
    return None #Pas aan! Terugkeerwaarde is hier niet None
  

#Print een overzicht met per bedrijf alle bezoekers in alfabetische volgorde
def printBedrijfsbezoekOverzicht():
    #ToDo
    return None #Pas aan! Terugkeerwaarde is hier niet None
        


def consoleApplicatie():
    boodschap = "1: Ga na of een student meegaat naar een bepaald bedrijf\n"
    boodschap += "2: Toon een overzicht van alle bezoekers voor een bepaald bedrijf\n"
    boodschap += "3: Toon een overzicht van alle bedrijfsbezoeken\n"
    boodschap += "0: sluit af\n"
    boodschap += "Invoer: "
    
    invoerGetal = int(input(boodschap)) 
    
    while invoerGetal != 0:
        if invoerGetal == 1:
            print("ToDo: Invoer 1")
        elif invoerGetal == 2:
            print("ToDo: Invoer 2")
        elif invoerGetal == 3:
            print("ToDo: Invoer 3")
        else:
            print("Ongeldige invoer!")
            
        invoerGetal = int(input(boodschap)) #Nieuwe invoer inlezen


def main():
    global bedrijfsbezoekenOverzicht
    #Globale variabele die door alle functies gelezen kan worden
    #Bevat na uitvoeren van 'leesInformatieIn()' alle informatie over de bedrijfsbezoeken
    #Merk op: als je binnen een functie een globale variabele wil aanpassen moet je dit aangeven met keywoord 'global'
    #Het lezen van een globale variabele kan altijd, dus daarvoor moet keywoord 'global' niet gebruikt worden
    #Voor dit practicum wordt deze globale variabele enkel aangepast in functie 'leesInformatieIn'.
    #Je hoeft dus in geen enkele andere functie het 'global' keywoord te gebruiken
    bedrijfsbezoekenOverzicht = {} #Initieel: leeg dictionary

    studentenlijstFileLocatie = "Studentenlijst.txt" #pas dit aan naar de juiste locatie van de studentenlijst
    bedrijfFileLocatie = "Bedrijvenlijst.txt" #pas dit aan naar de juiste locatie van de bedrijvenlijst
    leesInformatieIn(studentenlijstFileLocatie,bedrijfFileLocatie)
    consoleApplicatie()
    
    
main() 
        