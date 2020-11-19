class Dier:
    def __init__(self, soort, naam, leeftijd):
        self.setSoort(soort)  # string
        self.setNaam(naam)  # float
        self.setLeeftijd(leeftijd)

    def setNaam(self, naam):
        self._naam = naam

    def setSoort(self, soort):
        self._soort = soort

    def setLeeftijd(self, leeftijd):
        self._leeftijd = leeftijd

    def getNaam(self):
        return self._naam

    def getLeeftijd(self):
        return self._leeftijd

    def __repr__(self):
        resultaat = "Diersoort " + str(self._soort) + " met naam " + str(self._naam)
        resultaat += " heeft leeftijd " + str(self._leeftijd)
        return resultaat


class Verzorger:
    def __init__(self, naam, leeftijd):
        self.setNaam(naam)
        self.setLeeftijd(leeftijd)
        self._aantalDieren = 0
        self._setDieren = set()

    def setNaam(self, naam):
        Verzorger._naam = naam

    def setLeeftijd(self, leeftijd):
        Verzorger._leeftijd = leeftijd

    def addDier(self, dier):
        self._setDieren.add(dier)
        self._aantalDieren += 1

    def getSetDieren(self):
        return set(self._setDieren)


class Zoogdier(Dier):

    def __init__(self, soort, naam, leeftijd, aantal_nipples, aantal_botten):
        super().__init__(soort, naam, leeftijd)
        self._aantalNipples = aantal_nipples
        self._aantalBotten = aantal_botten

    def get_aantal_nipples(self):
        return self._aantalNipples

    def get_aantal_botten(self):
        return self._aantalBotten

    def set_aantal_nipples(self, aantal_nipples):
        self._aantalNipples = aantal_nipples

    def set_aantal_botten(self, aantal_botten):
        self._aantalBotten = aantal_botten


def main():
    biggie = Dier("Beer", "Biggie", 25.0)
    print(biggie)
    jarne = Verzorger("Jarne", 23.0)
    print(jarne)
    jarne.addDier(biggie)
    print(jarne.getSetDieren())


main()
