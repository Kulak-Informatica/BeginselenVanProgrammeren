##  Klasse die vakken voorstelt
#   eigenschappen: naam, aantal studiepunten en factor
#
class Vak:

    ##  Constructor
    #   @param naam
    #   @param studiepunten
    #   @param factor
    #
    def __init__(self,naam, studiepunten, factor=0.5):
        self.setNaam(naam)
        self.setStudiepunten(studiepunten)
        self.setFactor(factor)


    ##  Geeft de naam terug
    #
    def getNaam(self):
        return self._naam

    ##  Stelt de naam in
    #   @param naam
    #
    def setNaam(self,naam):
        self._naam = naam

    ##  Geeft de factor terug
    #
    def getFactor(self):
        return self._factor

    ##  Stelt de factor in, indien niet geldig wordt default 0.5 genomen
    #   @param factor: de factor, default = 0.5
    #
    def setFactor(self,factor=0.5):
        if 0 <= factor <= 1:
            self._factor = factor
        else:
            self._factor = 0.5




    ##  Geeft het aantal studiepunten terug
    #
    def getStudiepunten(self):
        return self._studiepunten

    ##  Stelt het aantal studiepunten in, indien niet geldig wordt default 3 genomen
    #   @param stp: het aantal studiepunten, default = 3
    #
    def setStudiepunten(self,stp=3):
        if 0 <= stp <= 60:
            self._studiepunten = stp
        else:
            self._studiepunten = 3































##  Klasse die examens voorstelt
#   eigenschappen: vak en twee scores
#
class Examen:

    ##  Constructor
    #   @param vak
    #   @param puntenTheorie
    #   @param puntenOefeningen
    #
    def __init__(self, vak, puntenTheorie, puntenOefeningen):
        self._vak = vak
        if 0 <= puntenTheorie <= 20 :
            self._puntenTheorie = puntenTheorie
        else:
            self._puntenTheorie = 0
        if 0 <= puntenOefeningen <= 20 :
            self._puntenOefeningen = puntenOefeningen
        else:
            self._puntenOefeningen = 0

    ##  Stelt het vak in
    #   @param vak
    #
    def setVak(self,vak):
        self._vak=vak

    ##  Geeft het vak terug
    #
    def getVak(self):
        return self._vak

    ##  Stelt de punten voor de theorie in, 0 indien niet geldig
    #   @param p, default = 0
    #
    def setPuntenTheorie(self,p=0):
        if 0 <= p <= 20 :
            self._puntenTheorie = p
        else:
            self._puntenTheorie = 0




    ##  Geeft de punten voor de theorie terug
    #
    def getPuntenTheorie(self):
        return self._puntenTheorie

    ##  Stelt de punten voor de oefeningen in, 0 indien niet geldig
    #   @param p, default = 0
    #
    def setPuntenOefeningen(self,p=0):
        if 0 <= p <= 20 :
            self._puntenOefeningen = p
        else:
            self._puntenOefeningen = 0

    ##  Geeft de punten voor de oefeningen terug
    #
    def getPuntenOefeningen(self):
        return self._puntenOefeningen

    ##  Berekent de score voor dit vak
    #   @return: het gewogen gemiddelde van de punten
    #
    def berekenScore(self):
        return round(self._puntenTheorie * self._vak.getFactor() + self._puntenOefeningen * (1-self._vak.getFactor()))




















##  Klasse stelt studenten voor
#   eigenschappen: voornaam, familienaam, en lijst examens
#
class Student:

    ##  Constructor
    #   @param voornaam
    #   @param familienaam
    #
    def __init__(self,voornaam, familienaam):
        # Als (beter) alternatief kan er ook met setters gewerkt worden
        self._voornaam = voornaam
        self._familienaam = familienaam
        self._examens = []

    ##  Geeft de voornaam terug
    #
    def getVoornaam(self):
        return self._voornaam

    ##  Geeft de familienaam terug
    #
    def getFamilienaam(self):
        return self._familienaam

    ##  Voegt een examen toe aan de lijst examens
    #   @param examen
    #
    def addExamen(self,examen):
        self._examens.append(examen)

    ##  Berekent de totale score van een student
    #   return: de gemiddelde score, gewogen naar aantal studiepunten
    #
    def getTotaleScore(self):
        totaalAantalStudiepunten = 0
        totaleScore = 0
        for examen in self._examens:
            studiepunten = examen.getVak().getStudiepunten()
            totaalAantalStudiepunten += studiepunten
            totaleScore += (examen.berekenScore()*studiepunten)
        # Bereken de gewogen score in een percentage.
        score = (totaleScore / totaalAantalStudiepunten)*100/20
        return score