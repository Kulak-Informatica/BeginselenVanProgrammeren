# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:54:03 2020

@author: Karl Van Holder    Ingenieurswetenschappen
         Thibaut Deliever   Informatica

@document: Beginselen van programmeren: Practica 2
           Klassen.py
"""

class magazijnbeheer:
    def __init__(self):
        self._voorraad = dict()
        
    def getMagazijn(self):
        return self._voorraad
    
    def getOverzicht(self):
        Boodschap = "\tOverzicht van de volledige stock"
        print(f"\t{'#'*len(Boodschap)}")
        print(Boodschap)
        print(f"\t{'#'*len(Boodschap)}")
        
        for naam, product in self._voorraad.items():
            print(f"\tOverzicht voor {naam}:")
            print(f"\t\tAankoopprijs: € {product.getProductAankoopprijs()}")
            print(f"\t\tVerkoopprijs: € {product.getProductVerkoopprijs()}")
            print(f"\t\tAantal in stock: {product.getProductAantal()}")
            print(f"\t\tVerkoopwaarde stock: € {product.getProductWaarde()}")
            print(f"\t\tAantal verkocht: {product.getProductVerkocht()}")
            print(f"\t\tTotale winst op product: € {round(product.getProductWinst(), 4)}")
            print()
        
        Boodschap = '\tInfo over de volledige stock:'
        print(f"\t{'#'*len(Boodschap)}")
        print(Boodschap)
        print(f"\t{'#'*len(Boodschap)}")    
        
        print(f"\tTotale verkoopwaarde stock: € {self.getStockWaarde()}")
        print(f"\tTotale winst: € {self.getTotaleWinst()}")
                
    def getProducttype(self, naam):
        return self._voorraad[naam]
    
    def getStockWaarde(self):
        som = 0
        for Naam, Product in self._voorraad.items():
            som += Product.getProductWaarde()
        return som
    
    def getTotaleWinst(self):
        som = 0
        for Naam, Product in self._voorraad.items():
            som += Product.getProductWinst()
        return som
    
    def addProduct(self, naam, aankoopp, verkoopp):
        if naam not in self._voorraad.keys():
            self._voorraad[naam] = producten(naam, aankoopp, verkoopp)
            print(f"\t'{naam}' succesvol toegevoegd aan het magazijn")
        else:
            print(f"\t** Error Magazijn: Product bestaat al **")

    def delProduct(self, naam):
        del self._voorraad[naam]
        print(f"\t'{naam}' succesvol verwijderd uit het magazijn")
        
    def verwerkLevering(self, product, aantal):
        if product in self._voorraad.keys():
            self._voorraad[product].addProductAantal(aantal)
            print(f"\tLevering van '{product}' succesvol verwerkt in het magazijn")
        else:
            print(f"\t** Error Magazijn: Producttype bestaat nog niet **")
        
    def verwerkBestelling(self, product, aantal):
        self._voorraad[product].verwerkBestelling(aantal)
    
    def berekenWinst(self, product, aantal):
        vk = self._voorraad[product].getProductVerkoopprijs()
        ak = self._voorraad[product].getProductAankoopprijs()
        return aantal * (vk-ak)
    
    
class producten:
    def __init__(self, naam, aankoopp, verkoopp):
        self._naam = naam
        self._aankoopprijs = aankoopp
        self._verkoopprijs = verkoopp
        self._aantal = 0
        self._verkocht = 0
        
    def getProductNaam(self):
        return self._naam
    
    def getProductAankoopprijs(self):
        return self._aankoopprijs
    
    def getProductVerkoopprijs(self):
        return self._verkoopprijs
    
    def getProductAantal(self):
        return self._aantal
    
    def getProductVerkocht(self):
        return self._verkocht
    
    def getProductWaarde(self):
        return self._aantal * (self._verkoopprijs)
    
    def getProductWinst(self):
        return round(self._verkocht * (self._verkoopprijs - self._aankoopprijs), 4)
    
    def getProductData(self):
        return self._naam, self._aankoopprijs, self._verkoopprijs, self._aantal, self._verkocht
    
    def addProductAantal(self, aantal):
        self._aantal += aantal
        
    def verwerkBestelling(self, aantal):
        if self._aantal < aantal:
            print("\t** Error Magazijn: Te weinig voorraad om de bestelling te verwerken! **")
            return 1
        else:
            self._aantal -= aantal
            self._verkocht += aantal
            print("\tBestelling verwerkt in het magazijn")
            return None
            

class klantenbeheer:
    def __init__(self):
        self._systeem = dict()
        
    def getKlantenSysteem(self):
        return self._systeem
    
    def getKlant(self, naam):
        return self._systeem[naam]
        
    def getOverzicht(self):
        Boodschap = "\tOverzicht van het klantensysteem"
        print(f"\t{'#'*len(Boodschap)}")
        print(Boodschap)
        print(f"\t{'#'*len(Boodschap)}")
        print(f"\tTotaal aantal Klanten: {len(self._systeem.keys())}")
        print("\tOverzicht van de klanten:")
        for naam, klant in self._systeem.items():
            print(f"\t Overzicht voor {naam}:")
            print(f"\t   Naam: {klant.getKlantNaam()}")
            print(f"\t   Klantennummer: {klant.getKlantennummer()}")
            print(f"\t   Winst op de klant: € {round(klant.getKlantWinst(), 4)}")
            print("\t   Bestellingsgeschiedenis:")
            bestelling = klant.getKlantBestellingen()
            for i in bestelling:
                print(f"\t    * {i.getBestellingProduct()}: {i.getBestellingAantal()}")
            print()
    
    def addKlant(self, naam):
        #rekening houden met bestaande klanten met zelfde naam
        self._systeem[naam] = klant(naam)
        print(f"\tKlant '{naam}' succesvol toegevoegd aan het klantensysteem")
        
    def delKlant(self, naam):
        del self._systeem[naam]
        print(f"\tKlant '{naam}' succesvol verwijderd uit het klantensysteem")


class klant:
    nr = 1
    def __init__(self, naam):
        self._naam = naam
        self._klantennummer = klant.nr
        self._bestellingen = []
        self._winst = 0
        klant.nr += 1
    
    def getKlantNaam(self):
        return self._naam
    
    def getKlantennummer(self):
        return self._klantennummer
    
    def getKlantBestellingen(self):
        return self._bestellingen       
    
    def getKlantWinst(self):
        return self._winst
    
    def getKlantOverzicht(self):
        print(f"\tNaam: {self._naam}")
        print(f"\tKlantennummer: {self._klantennummer}")
        print(f"\tWinst op de klant: € {self._klantennummer}")
        print("\tBestellingsgeschiedenis:")
        for i in self._bestelling:
            print(f"\t * {i.getBestellingProduct()}: {i.getBestellingAantal()}")
        
        
    def addKlantBestelling(self, mag, product, aantal):
        data = bestelling(mag, aantal, product)
        ms = mag.verwerkBestelling(product, aantal)
        winst = data.getBestellingWinst()
        #print("BESTELLINGSDATA:", data.getBestellingData(), "\nMS:", ms, "\nWINST:", winst)
        if ms == None:
            self._bestellingen += [data]
            self._winst += winst
            
            #print("BESTELLINGSLIJST:", self._bestellingen)
        else:
            print("\t** Error Klantenbeheer: Bestelling kan niet worden uitgevoerd! **")
        
    
class bestelling:
    def __init__(self, mag, aantal, product):
        self._aantal = aantal
        self._product = product
        winst = mag.berekenWinst(product, aantal)
        self._winst = winst

    def getBestellingAantal(self):
        return self._aantal
    
    def getBestellingProduct(self):
        return self._product
    
    def getBestellingWinst(self):
        return self._winst
    
    def getBestellingData(self):
        return [(self._product, self._aantal), self._winst]