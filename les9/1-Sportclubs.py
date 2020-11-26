# Please note: I have NOT tested ANY of this.
class Club:
    # - Initialise -
    def __init__(self, naam, ledenlijst):
        self.naam = naam
        self.ledenlijst = ledenlijst

    # - Getters -
    def getNaam(self):
        return self.naam

    def getLedenlijst(self):
        return self.ledenlijst


class Lid:
    # - Initialise -
    def __init__(self, naam, id):
        self.naam = naam
        self.registratienummer = id

    # - Getters -
    def getNaam(self):
        return self.naam

    def getRegistratienummer(self):
        return self.registratienummer



class Wedstrijd:
    # - Initialise -
    def __init__(self, lid_resultaat):
        self.leden_en_resultaten = lid_resultaat

    # - Getters -
    def getLeden(self):
        return list(self.leden_en_resultaten.keys())

    def getLedenEnResultaten(self):
        return self.leden_en_resultaten


class Amateurclub(Club):
    # - Initialise -
    def __init__(self, naam, leden, activiteiten):
        super().__init__(naam, leden)
        self.activiteiten = activiteiten

    # - Getters -
    def getActiviteiten(self):
        return self.activiteiten


class Profclub(Club):
    # - Initialise -
    def __init__(self, naam, leden, wedstrijden):
        super().__init__(naam, leden)
        self.wedstrijdenlijst = wedstrijden

    # - Getters -
    def getWedstrijden(self):
        return self.wedstrijdenlijst

    # - Misc -
    def deelnamesVanLid(self, lid):
        # stel dat het lid niet deel is van de club, geef een lege lijst.
        # Hier konden we mogelijks een foutmelding laten afgaan via
        # raise ValueError(str(lid) + " is geen clublid")
        if lid not in self.ledenlijst:
            return []

        deelnames = []
        for wedstrijd in self.wedstrijdenlijst:
            if lid in wedstrijd:
                deelnames.append(wedstrijd)
        return deelnames

    def alleInTop10(self):
        # De wedstrijden waarin alle deelnemende leden van de club in de top 10 zitten:
        goede_wedstrijden = []

        # We bekijken elke wedstrijd in de lijst van de wedstrijden waar aan zijn deelgenomen door de club
        for wedstrijd in self.wedstrijdenlijst:

            # We gaan er eerst van uit dat elk lid in de top 10 zit
            alle_in_10 = True

            # We bekijken elk lid uit de club, en testen of deze een deelnemer is.
            for lid in self.ledenlijst:
                # Stel dat er een lid is die deelnemer is, en deze zit niet in de top 10, is de hypothese fout.
                # Stop de lus.
                if lid in wedstrijd.getLeden() and wedstrijd.getLedenEnResultaten()[lid] > 10:
                    alle_in_10 = False
                    break

            # Als de hypothese nooit bewezen is van fout te zijn, voegen we de wedstrijd toe aan de lijst.
            if alle_in_10:
                goede_wedstrijden.append(wedstrijd)

        # Na de uiterste for lus hebben we de lijst van alle wedstrijden met alle deelnemers van de club in de top 10.
        return goede_wedstrijden


# Aangezien er een lijst nodig is met amateur- en profclubs, moet dit dus een aparte functie zijn.
def amateurclubsMetTweeProfs(amateurclubs, profclubs):
    """
    Test alle amateurclubs om te kijken of er minstens twee leden zijn die ook in een profclub zitten.
    :param amateurclubs: Lijst van alle amateurclubs
    :param profclubs: Lijst van alle profclubs
    :return: Lijst van alle amateurclubs met minstens twee leden uit profclubs
    """
    geldige_amateurclubs = []

    # Haal alle leden uit de profclubs en verzamel ze in een lijst
    profspelers = set()
    for club in profclubs:
        set().update(club.getLedenlijst)

    # bekijk alle amateurclubs
    for club in amateurclubs:

        aantal_profs = 0
        minstens_twee_profs = False

        # bekijk alle leden, of ze in een profclub zitten.
        for lid in club.getLedenlijst():
            if lid in profspelers:
                aantal_profs += 1

            # als er twee zijn, is de club geldig en mag in de lijst. Verder leden checken heeft geen nut.
            if aantal_profs == 2:
                minstens_twee_profs = True
                break

        if minstens_twee_profs:
            geldige_amateurclubs.append(club)

    return geldige_amateurclubs


def main():
    pass
