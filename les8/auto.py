## Klasse stelt auto's voor, met een bepaald verbruik en hoeveelheid brandstof
#
class Auto:

    ## constructor
    #   @param verbruik
    #
    def __init__(self,verbruik):
        self._verbruik = verbruik
        self._tankinhoud = 0

    ## Geeft de inhoud van de tank terug
    #
    def getTankinhoud(self):
        return self._tankinhoud

    ## Tankt een gegeven hoeveelheid brandstof bij
    #   @param hoeveelheid
    #
    def tank(self,hoeveelheid):
        self._tankinhoud += hoeveelheid

    ## Rijdt een gegeven afstand, en verbruikt brandstof
    #   @param afstand
    #
    def rij(self,afstand):
        self._tankinhoud -= self._verbruik * afstand / 100
        # Is het negatief geworden: maak er dan nul van.
        if self._tankinhoud < 0:
            self._tankinhoud = 0
        # Alternatief kun je ook eerst testen of je de volledige afstand kan rijden
        # met de resterende tankinhoud. Indien niet maak je deze dan ook gewoon nul.
