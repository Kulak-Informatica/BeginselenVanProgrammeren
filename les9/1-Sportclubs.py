# Please note: I have NOT tested ANY of this.
# Also note: I didn't stick to cycling only. These are clubs for all types of sports. Why?
# ....I was an idiot, that's why.
class Lid:

    _idnumber = 0

    # - Initialise -
    def __init__(self, naam):
        self.naam = naam
        self.registratienummer = Lid._idnumber
        Lid._idnumber += 1

    # - Getters -
    def getNaam(self):
        return self.naam

    def getRegistratienummer(self):
        return self.registratienummer

    def __repr__(self):
        return "Lid " + self.naam


# We moeten niks bijhouden voor deze klassen :(
class Event:
    pass


class Activiteit(Event):
    pass


class Uitstap(Event):
    pass


class Wedstrijd(Event):

    # Adding this in so I can keep track of which competition is which
    _wedstrijd_id = 0

    # - Initialise -
    def __init__(self, lid_resultaat):
        self.leden_en_resultaten = lid_resultaat
        self.wedstrijd_id = Wedstrijd._wedstrijd_id
        Wedstrijd._wedstrijd_id += 1

    # - Getters -
    def getLeden(self):
        return list(self.leden_en_resultaten.keys())

    def getLedenEnResultaten(self):
        return self.leden_en_resultaten

    def __repr__(self):
        return "Wedstrijd " + str(self.wedstrijd_id)


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

    def __repr__(self):
        return "*Club* " + self.naam


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
            if lid in wedstrijd.getLeden():
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
        ledenlijst = club.getLedenlijst()
        profspelers.update(ledenlijst)

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
    # Random bullshit, GO

    # - Leden -
    henry = Lid("Henry")
    julie = Lid("Julie")
    manon = Lid("Manon")
    amber = Lid("Amber")  # up till now they're all 5 letter names. Let's keep it going.
    jerry = Lid("Jerry")
    shawn = Lid("Shawn")
    dimme = Lid("Dimme")  # self-insert, with lucky 7
    drake = Lid("Drake")
    jeoff = Lid("Jeoff")
    robbe = Lid("Robbe")  # sommige van deze namen zijn mensen die ik ken. Puur toeval. I swear. (pls dont kill me)

    # - Events -
    # * Activiteiten en uitstappen *
    club_competitie = Activiteit()
    nationale_training = Uitstap()

    # * Wedstrijden *
    karate_vlaams = Wedstrijd({dimme: 1, robbe: 2, manon: 3})  # sorry manon, maar dit is de enige keer dat je voorkomt
    tennis_vlaams = Wedstrijd({jeoff: 1, amber: 2, jerry: 3})
    tennis_belgisch = Wedstrijd({jeoff: 1, amber: 2, dimme: 3, jerry: 17})
    # legend: {karate_vlaams: 0, tennis_vlaams: 1, tennis_belgisch: 2}

    # - Amateurclubs -
    karate_waregem = Amateurclub("KC Waregem", [dimme, julie, shawn, drake], [club_competitie, nationale_training])
    tennis_kortrijk = Amateurclub("TC Kortrijk", [shawn, jeoff, amber, jerry], [club_competitie, nationale_training])

    # - Profclubs -
    karate_nationale_club = Profclub("NatKClub", [dimme, robbe, henry, jeoff], [karate_vlaams])
    tennis_nationale_club = Profclub("NatTClub", [dimme, jeoff, amber, jerry], [tennis_vlaams, tennis_belgisch])

    # - Clublijsten -
    amateurclubs = [karate_waregem, tennis_kortrijk]
    profclubs = [karate_nationale_club, tennis_nationale_club]

    # - And finally: the test itself -

    # TEST 1 - Alle wedstrijden waaraan bepaald lid heeft deelgenomen:
    print(tennis_nationale_club.deelnamesVanLid(dimme))  # expected result: [tennis_belgisch (ID 2)]
    print(tennis_nationale_club.deelnamesVanLid(amber))  # expected result: [tennis_vlaams, tennis_belgisch (ID 1, 2)]

    # TEST 2 - Wedstrijden waarvan deelnemende leden van profclub alle in top 10:
    print(karate_nationale_club.alleInTop10())  # expected result: [karate_vlaams (ID 0)]
    print(tennis_nationale_club.alleInTop10())  # expected result: [tennis_vlaams (ID 1)]

    # TEST 3 - Amateurclubs met minstens twee leden in profclub(s):
    print(amateurclubsMetTweeProfs(amateurclubs, profclubs))  # expected result: [tennis_kortrijk]
# -- end of main() ------------------------------------------------------------------------


main()
