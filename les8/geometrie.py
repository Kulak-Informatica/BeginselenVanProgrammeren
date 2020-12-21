from math import pi

##  Klasse die cirkels voorstelt
#   eigenschappen: straal
#
class Cirkel:

    ##  Constructor
    #   @param straal
    #
    def __init__(self,straal):
        self._straal = straal

    ##  Geeft de straal van de cirkel terug
    #
    def getStraal(self):
        return self._straal

    ##  Berekent de omtrek van de cirkel
    #   @return: straal*2*pi
    #
    def berekenOmtrek(self):
        return self._straal*2*pi

    ##  Berekent de oppervlakte van de cirkel
    #   @return: straal*straal*pi
    #
    def berekenOppervlakte(self):
        return self._straal**2*pi















##  Klasse Cilinder
#   eigenschappen: grondvlak (cirkel) en hoogte
#
class Cilinder:

    ##  Constructor
    #   @param: grondvlak
    #   @param: hoogte
    #
    def __init__(self, straal, hoogte):
        self._grondvlak = Cirkel(straal)
        self._hoogte = hoogte

    ##  Berekent de oppervlakte van de cilinder
    #   @return: grondvlak.berekenOppervlakte()*2 + grondvlak.berekenOmtrek()*hoogte
    #
    def berekenOppervlakte(self):
        return self._grondvlak.berekenOppervlakte()*2 + self._grondvlak.berekenOmtrek()*self._hoogte

    ##  Berekent de inhoud van de cilinder
    #   @return: grondvlak.berekenOppervlakte()*hoogte
    #
    def berekenVolume(self):
        return self._grondvlak.berekenOppervlakte() * self._hoogte
