# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:57:08 2020

@author: Karl Van Holder    Ingenieurswetenschappen
         Thibaut Deliever   Informatica

@document: Beginselen van programmeren: Practica 2
           Main.py
          
@deadline: 13/12 - 23u59

@readme: Indien de console opgestart is, raden wij aan om optie 2 te kiezen om te starten...
	 Zo heeft het programma al een 'basis' om verdere functies op te testen :)

	 Wij hebben ook Opdracht 4 verwerkt in ons script (Optie 19). Wij hebben hierbij geen
	 tot weinig problemen ondervonden en hopen dat dit geen moeilijkheid met zich meebrengt
	 doordat het verwerkt zit in onze main.py
"""

## Imports
import os
import time
import pickle
from Klassen import *


## Globale variabelen
magazijn = dict()
klantenBeheer = dict()


## Functies
def simulatie(start=True):
    """
    De simulatie die werd gegeven als voorbeeld in de opgave

    Parameters
    ----------
    start : boolean
        Eventueel waardes gebruiken als start initiele data voor het programma.
        Hierbij worden al dan niet de globale variabelen aangepast
    
    Returns
    -------
    None

    stappenplan
    -----------
    1.  Maak een nieuw magazijn aan
    2.  Voeg 3 producttypes toe aan het magazijn.
         a. Appel: inkoopprijs €1 – verkoopprijs €1.5
         b. Peer: inkoopprijs €1.5 – verkoopprijs €2.5
         c. Banaan: inkoopprijs €0.5 – verkoopprijs €0.7
    3.  Er worden 50 appels, 100 peren en 10 bananen geleverd.
    4.  De magazijnmanager vraagt de verkoopwaarde van de appels op (print deze waarde
        op de standaarduitvoer)
    5.  De magazijnmanager vraagt de verkoopwaarde van de volledige stock op (print deze
        waarden op de standaarduitvoer)
    6.  Maak 2 klanten aan
    7.  Klant 1 koopt 10 appels
    8.  Klant 2 koopt 5 peren
    9.  De magazijnmanager vraagt de gemaakte winst op appels op (print deze waarde op
        de standaarduitvoer)
    10. De magazijnmanager vraagt de totale winst op (print deze waarde op de
        standaarduitvoer)
    11. Klant 1 koopt 20 peren
    12. Maak een derde klant aan
    13. Klant 3 koopt 5 bananen
    14. De magazijnmanager vraagt de magazijninfo op (print alle info over het magazijn:)
    """
    #INIT
    if start:
        global magazijn
        global klantenBeheer
    
    magazijn = magazijnbeheer()
    klantenBeheer = klantenbeheer()
    
    #1
    print('#1 \tAanmaken van een nieuw magazijn')
    
    #2
    print('#2 \tToevoegen van producttypes appel, peer en banaan aan het magazijn')  
    magazijn.addProduct("Appel", 1, 1.5)
    magazijn.addProduct("Peer", 1.5, 2.5)
    magazijn.addProduct("Banaan", 0.5, 0.7)

    #3
    print('#3 \tVerwerken van leveringen van 50 appels, 100 peren en 10 bananen')
    magazijn.verwerkLevering("Appel", 50)
    magazijn.verwerkLevering("Peer", 100)
    magazijn.verwerkLevering("Banaan", 10)    
    
    #4
    print('#4 \tVerkoopwaarde appels opvragen')
    product = magazijn.getProducttype("Appel")
    waarde = round(product.getProductWaarde(), 4)
    print(f'\tDe verkoopwaarde van de huidige stock appels is: €{waarde}')
    
    #5
    print('#5 \tVerkoopwaarde van de volledige stock opvragen')
    waarde = round(magazijn.getStockWaarde(), 4)
    print(f'\tDe verkoopwaarde van de volledige stock is: € {waarde}')
    
    #6
    print('#6 \tAanmaken van 2 klanten')
    klantenBeheer.addKlant("Klant 1")
    klantenBeheer.addKlant("Klant 2")
    
    #7
    print('#7 \tKlant 1 koopt 10 appels')
    klant = klantenBeheer.getKlant("Klant 1")
    klant.addKlantBestelling(magazijn, "Appel", 10)
    
    #8
    print('#8 \tKlant 2 koopt 5 peren')
    klant = klantenBeheer.getKlant("Klant 2")
    klant.addKlantBestelling(magazijn, "Peer", 5)
    
    #9
    print("#9 \tTotale winst op appels opvragen")
    product = magazijn.getProducttype("Appel")
    waarde = product.getProductWinst()
    print(f"\tTotale winst op appels: € {waarde}")
    
    #10 
    print("#10\tTotale winst van de stock opvragen")
    waarde = magazijn.getTotaleWinst()
    print(f"\tTotale winst stock: € {waarde}")
    
    #11
    print("#11\tKlant 1 koopt 20 peren")
    klant = klantenBeheer.getKlant("Klant 1")
    klant.addKlantBestelling(magazijn, "Peer", 20)
    
    #12
    print("#12\tAanmaken van een derde klant")    
    klantenBeheer.addKlant("Klant 3")
    
    #13
    print("#13\tKlant 3 bestelt 5 bananen")
    klant = klantenBeheer.getKlant("Klant 3")
    klant.addKlantBestelling(magazijn, "Banaan", 5)
    
    #14
    print("#14\tPrinten van alle info over het magazijn")
    magazijn.getOverzicht()


def initData(backup=False):
    """
    De initializering van de data bij opstart

    Parameters
    ----------
    backup : boolean
        Eventueel backup gebruiken als start initiele data voor het programma.
        Hier worden dan eventueel andere bestanden ingeladen
        
    Returns
    -------
    None
    """
    
    ## try except doen als de file niet gevonden/te openen valt
    print("** INLEZEN VAN DE DATABASES **")
    global magazijn
    global klantenBeheer
    
    
    try:
        if backup:
            magazijn = pickle.load( open( "./DB/DBMagazijn_backup.p", "rb" ) )
            klantenBeheer = pickle.load( open( "./DB/DBKlantenbeheer_backup.p", "rb" ) )
        else:
            magazijn = pickle.load( open( "./DB/DBMagazijn.p", "rb" ) )
            klantenBeheer = pickle.load( open( "./DB/DBKlantenbeheer.p", "rb" ) )
        
        print("\t** Inlezen succesvol **")
    except:
        if backup:
            print("\t** Error inlezen: Geen backup_DB gevonden **")
        else:
            print("\t** Error inlezen: Geen DB gevonden **")
            print("\t** Nieuwe DB genereren... **")
        
        magazijn = magazijnbeheer()
        klantenBeheer = klantenbeheer()
        

def drukBoodschap(mes, lengte, title=False):
    """
    Een functie die een opmaak weergeeft aan een boodschap die moet opvallen.
    Dit kunnen onderandere titels en dergelijke zijn.

    Parameters
    ----------
    mes : string
        De boodschap in string-vorm
    lengte : integer
        Het aantal karakters de nodige opmaak moet hebben
    title : Boolean
        Een parameter die aangeeft als we met de hoofdtitel bezig zijn van het programma.
        Er wordt dan indien nodig een ander symbool gebruikt om dit te accentueren.
    
    Returns
    -------
    None
    """
    symbol = "-"
    if title:
        symbol = "#"
        
    print()
    print(symbol*lengte)
    print(mes)
    print(symbol*lengte)


def checkedInputMenu(Opties):
    """
    Een functie die de inputs checked en desnoods opnieuw opvraagt binnen bepaalde grenswaarden.
    Deze functie wordt gebruikt bij het kiezen van menu-opties

    Parameters
    ----------
    Opties : integer
        Het aantal mogelijke opties het menu bevat om dynamisch de grenswaardes aan te passen
    
    Returns
    -------
    x : integer
        Een optienummer die het menu kan bevatten
    """
    mogelijkheden = [str(i) for i in range(Opties + 1)]
    
    x = input("> ")
    while x not in mogelijkheden:
        x = input("Geef een geldige optie! \n> ")
        
    return int(x)
    

def checkedInputAantal(multiple=False):
    """
    Een functie die de inputs checked en desnoods opnieuw opvraagt binnen bepaalde grenswaarden.
    Deze functie wordt gebruikt bij het kiezen van een bepaald aantal van een product

    Parameters
    ----------
    multiple : boolean
        Boolean die bijhoudt als de functie meer dan 1 keer moet opnieuw opgevraagd worden.
        Hierbij verandert dan de input-vraag
        
    Returns
    -------
    x : integer
        Het geldig aantal-getal
    """
    if multiple:
        x = input("Geldig aantal aub: ")
    else:
        x = input("Aantal: ")
        
    try:
        x = int(x)
        if x >= 0:
            return x
        checkedInputAantal(True)
    except:
        checkedInputAantal(True)
        

def shutdown(i=1):
    """
    Functie die tijdens het afsluiten wordt opgeroepen om een bepaalde procedure toe te passen
    Hierbij zal de data worden opgeslagen in een ./DB/*.p locatie

    Parameters
    ----------
    i : integer
        Getal dat bijhoudt hoeveel keer de functie is opgeroepen indien er fouten optraden.
        Hierbij is het maximum gedefinieerd op 3 probeersels om de data op te slaan
    Returns
    -------
    None
    """
    
    print("** Opslaan en afsluiten **")
    try:
        if i <= 3:
            pickle.dump(magazijn, open( "./DB/DBMagazijn.p", "wb" ) )
            pickle.dump(klantenBeheer, open( "./DB/DBKlantenbeheer.p", "wb" ) )
            print("\t** Gegevens opgeslagen **")
        else:
            print("\t** GEGEVENS OPSLAAN MISLUKT **")
        
    except:
        print("\t** Error shutdown: Er is een fout opgetreden tijdens het opslaan van de data **")
        print(f"\t** Opnieuw proberen ({i})... **\n")
        os.makedirs('./DB')
        shutdown(i+1)
    
    
def backup():
    """
    Een functie die na elke gekozen input-optie de data opslaat in een backup-file.
    Dit is op dezelfde locatie bij de andere database files met de vorm van de file: *.p

    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        pickle.dump(magazijn, open( "./DB/DBMagazijn_backup.p", "wb" ) )
        pickle.dump(klantenBeheer, open( "./DB/DBKlantenbeheer_backup.p", "wb" ) )
    except:
        pass
    
    
def readBackup():
    """
    Een functie die wordt opgeroepen indien de optie 'backup databases inladen' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    initData(True)


def sim1():
    """
    Een functie die wordt opgeroepen indien de simulatie werd opgevraagd zonder de data hierbij
    op te slaan
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    simulatie(False)
    
    
def sim2():
    """
    Een functie die wordt opgeroepen indien de simulatie werd opgevraagd met de data hierbij
    op te slaan
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    simulatie()


def addProduct():
    """
    Een functie die wordt opgeroepen indien de optie 'voeg een producttype toe' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        product = input("Product: ")
        aankp = float(input("Aankoopprijs: "))
        verkp = float(input("Verkoopprijs: "))
        magazijn.addProduct(product, aankp, verkp)
    except:
        print(f"\t** Error: Er is iets fout gelopen tijdens het toevoegen van het product '{product}' **")
    
    
def verwerkLevering():
    """
    Een functie die wordt opgeroepen indien de optie 'verwerk een levering' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        product = input("Product: ")
        aantal = checkedInputAantal()
        magazijn.verwerkLevering(product, aantal)
    except:
        print(f"\t** Error: Er is iets fout gelopen tijdens het verwerken van de levering van '{product}' **")
    
    
def addBestelling():
    """
    Een functie die wordt opgeroepen indien de optie 'verwerk een bestelling' werd gekozen.
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        naam = input("Klant: ")
        product = input("Product: ")
        aantal = checkedInputAantal()
        klant = klantenBeheer.getKlant(naam)
        klant.addKlantBestelling(magazijn, product, aantal)
    except:
        print(f"\t** Error: Er is iets fout gelopen tijdens het toevoegen van een bestelling aan klant '{naam}' **")

    
def getVerkoopw():
    """
    Een functie die wordt opgeroepen indien de optie 'Verkoopwaarde van een product opvragen' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        product = input("Product: ")
        magProduct = magazijn.getProducttype(product)
        waarde = magProduct.getProductWaarde()
        print(f"\tDe verkoopwaarde van de huidige stock '{product}' is: €{waarde}")
    except:
        print(f"\t** Error: Er is iets fout gelopen tijdens het opvragen van de verkoopwaarde van het product '{product}' **")


def getVerkoopwStock():
    """
    Een functie die wordt opgeroepen indien de optie 'Verkoopwaarde van de stock opvragen' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        waarde = magazijn.getStockWaarde()
        print(f"\tDe verkoopwaarde van de volledige stock is: € {waarde}")
    except:
        print("\t** Error: Er is iets fout gelopen tijdens het opvragen van de verkoopwaarde van de volledige stock **")
    
        
def getWinstProduct():
    """
    Een functie die wordt opgeroepen indien de optie 'Winst van een bepaald producttype opvragen' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        product = input("Product: ")
        magProduct = magazijn.getProducttype(product)
        waarde = magProduct.getProductWinst()
        print(f"\tTotale winst op '{product}': € {waarde}")
    except:
        print(f"\t** Error: Er is iets fout gelopen tijdens het opvragen van de totale winst van het product '{product}' **")

    
def getInfoProduct():
    """
    Een functie die wordt opgeroepen indien de optie 'Informatie opvragen over een bepaald producttype' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        product = input("Product: ")
        magProduct = magazijn.getProducttype(product)
        data = magProduct.getProductData()
        print(data)
    except:
        print(f"\t** Error: Er is iets fout gelopen tijdens het opvragen van de data over het product '{product}' **")

    
def getOverzichtMag():
    """
    Een functie die wordt opgeroepen indien de optie 'Overzicht van het magazijn opvragen' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        magazijn.getOverzicht()
    except:
        print("\t** Error: Er is iets fout gelopen tijdens het opvragen van het overzicht van het magazijn **")
   
    
def addKlant():
    """
    Een functie die wordt opgeroepen indien de optie 'Klant toevoegen aan het systeem' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        naam = input("Naam: ")
        klantenBeheer.addKlant(naam)
    except:
        print(f"\t** Error: Er is iets foutgelopen tijdens het toevoegen van de klant '{naam}' **")


def delKlant():
    """
    Een functie die wordt opgeroepen indien de optie 'Klant verwijderen uit het systeem' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        naam = input("Naam: ")
        if input(f"Bent u zeker om de klant '{naam}' te verwijderen? (j/n): ") == "j":
            klantenBeheer.delKlant(naam)
        else:
            print("\tVerwijderen geannuleerd")
    except:
        print(f"\t** Error: Er is iets foutgelopen tijdens het verwijderen van de klant '{naam}' **")


def delProduct():
    """
    Een functie die wordt opgeroepen indien de optie 'Verwijder een producttype uit het magazijn' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        product = input("Product: ")
        if input(f"Bent u zeker om het product '{product}' te verwijderen? (j/n): ") == "j":
            magazijn.delProduct(product)
        else:
            print("\tVerwijderen geannuleerd")
            
    except:
        print(f"\t** Error: Er is iets foutgelopen tijdens het verwijderen van het product '{product}' **")


def getOverzichtKlanten():
    """
    Een functie die wordt opgeroepen indien de optie 'Overzicht van het klantensysteem opvragen' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        klantenBeheer.getOverzicht()
    except:
        print("\t** Error: Er is iets fout gelopen tijdens het opvragen van het overzicht van het klantensysteem **")
    

def getInfoKlant():
    """
    Een functie die wordt opgeroepen indien de optie 'Informatie opvragen over een klant' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        naam = input("Naam: ")
        klant = klantenBeheer.getKlant(naam)
        klant.getKlantOverzicht()
    except:
        print(f"\t** Error: Er is iets fout gelopen tijdens het opvragen van het overzicht van de klant '{naam}' **")


def getGrootsteWinstKlant():
    """
    Een functie die wordt opgeroepen indien de optie 'Meest winstgevende klant' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        sys = klantenBeheer.getKlantenSysteem()
        maxKoper = ""
        maxBedrag = 0
        for naam, klant in sys.items():
            winst = klant.getKlantWinst()
            if maxBedrag < winst:
                maxBedrag = winst
                maxKoper = naam
        print(f"\tDe klant '{maxKoper}' heeft de meeste winst gegenereerd namelijk een bedrag van maar liefst € {maxBedrag}!")
    except:
        print("\t** Error: Er is iets fout gelopen tijdens het opvragen van de meest winstgevende klant **")


def getGrootsteWinstProduct():
    """
    Een functie die wordt opgeroepen indien de optie 'Meest winstgevend product opvragen' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    try:
        sys = magazijn.getMagazijn()
        maxProduct = ""
        maxBedrag = 0
        for naam, product in sys.items():
            winst = product.getProductWinst()
            if maxBedrag < winst:
                maxBedrag = winst
                maxKoper = naam
        print(f"\tHet product '{maxKoper}' heeft de meeste winst gegenereerd namelijk een bedrag van maar liefst € {maxBedrag}!")
    except:
        print("\t** Error: Er is iets fout gelopen tijdens het opvragen van de meest winstgevende klant **")


def getComplexiteit():
    """
    Een functie die wordt opgeroepen indien de optie 'Informatie tijdscomplexiteit' werd gekozen
    
    Parameters
    ----------
    None
        
    Returns
    -------
    None
    """
    mes = "\tHet berekenen van het meest winstgevend product en de meest winstgevende klant is gelijkaardig. "
    mes += "De tijdscomplexiteit van deze methodes hangen bijna volledig af van het aantal klanten 'K' of het "
    mes += "aantal producten 'P'. Doordat we éénmalig de volledige lijst met klanten of producten gaan doorlopen "
    mes += "en al onze getallen gekoppeld zijn aan deze elementen uit de lijst kunnen we de tijdscomplexiteit "
    mes += "definiëren met de formule 'K + K*b + k*v' waarbij b en v respectievelijk het aantal bewerkingen en "
    mes += "het aantal vergelijkingen zullen voorstellen. Deze complexiteit zal dus lineair zijn. "
    print(mes)


def console(p=5):
    """
    De consolefunctie die het opstarten weergeeft en het menu met de bijhorende mogelijkheid om 
    een getal in te lezen. Indien dit 0 is gaat de functie uit de loop springen en eindigen.
    
    Indien de applicatie wordt uitgebreid met extra functies dient u de functie aan te geven met bijhorend
    nummer in de variabele 'functies'. Dit doet u door de naam van de functie te geven als value in deze dictionary
    zonder de 'uitvoerings-haakjes'
    
    Parameters
    ----------
    p : integer
        aantal seconden pauze tussen 2 mogelijke commando's in het menu
        
    Returns
    -------
    None
    """
    functies = {1: sim1,
                2: sim2,
                3: readBackup,
                4: addProduct,
                5: delProduct,
                6: addKlant,
                7: delKlant,
                8: verwerkLevering,
                9: addBestelling,
                10:getVerkoopw,
                11:getVerkoopwStock,
                12:getWinstProduct,
                13:getInfoProduct,
                14:getInfoKlant,
                15:getOverzichtMag,
                16:getOverzichtKlanten,
                17:getGrootsteWinstProduct,
                18:getGrootsteWinstKlant,
                19:getComplexiteit
                }
    
    title = "Magazijnbeheer -- ©Karl & Thibaut"
    
    menu = "0.\tData opslaan en afsluiten\n"
    menu += "---\n"
    menu += "1.\tSimulatie afspelen (afzonderlijk)\n"
    menu += "2.\tSimulatie afspelen (simulatie als startgegevens gebruiken)\n"
    menu += "3.\tBackup databases inladen\n"
    menu += "4.\tVoeg een nieuw producttype toe\n"
    menu += "5.\tVerwijder een producttype uit het magazijn\n"
    menu += "---\n"
    menu += "6.\tKlant toevoegen aan het systeem\n" 
    menu += "7.\tKlant verwijderen uit het systeem\n"
    menu += "8.\tVerwerk een levering\n"
    menu += "9.\tVerwerk een bestelling\n"
    menu += "10.\tVerkoopwaarde van een product opvragen\n"
    menu += "---\n"
    menu += "11.\tVerkoopwaarde van de stock opvragen\n"
    menu += "12.\tWinst van een bepaald producttype opvragen\n"
    menu += "13.\tInformatie opvragen over een bepaald producttype\n"
    menu += "14.\tInformatie opvragen over een klant\n"
    menu += "15.\tOverzicht van het magazijn opvragen\n"
    menu += "---\n"
    menu += "16.\tOverzicht van het klantensysteem opvragen\n"
    menu += "17.\tMeest winstgevend product opvragen\n"
    menu += "18.\tMeest winstgevende klant opvragen\n"
    menu += "19.\tInformatie tijdscomplexiteit"
    
    lengteMenu = len(max(menu.split("\n"), key=len))
    lengteSpaties = lengteMenu // 2 - len("Menu")
    
    menuTitle = " " * lengteSpaties
    menuTitle += "MENU\n\n"
    menuTitle += menu
    
    drukBoodschap(title, len(title), True)
    drukBoodschap(menuTitle, lengteMenu)
    
    Opties = len(functies)
    
    nr = checkedInputMenu(Opties)
    while nr > 0:
        functies[nr]()
        
        time.sleep(p)
        drukBoodschap(menuTitle, lengteMenu)
        backup()
        nr = checkedInputMenu(Opties)
    

def main(p=5):
    """
    Main-functie die wordt opgeroepen bij het starten van het programma. Hierbij wordt eerst de data opgevraagd 
    door de init-functie waarna de console wordt opgeroepen en indien daar een cijfer 0 wordt gebruikt tijdens 
    de menukeuze zal de shutdown-functie worden uitgevoerd
    
    Parameters
    ----------
    p : integer
        aantal seconden pauze tussen 2 mogelijke commando's in het menu
        Standaard is dit 5 seconden.
        
    Returns
    -------
    None
    """        
    initData()
    console(p)
    shutdown()
    
    
main()