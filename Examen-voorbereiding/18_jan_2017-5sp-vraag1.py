# NOTE: never finished this.
# Dit is de opgave op toledo
# NIET die van in de box.
# Voor een of andere reden zijn ze verschillend...

def _in_minuten(time):
    """
    Zet een tuple met een tijd (uur, minuten) om in een int voor het totaal aantal minuten sinds 00:00
    :param time: tuple met de tijd
    :return: int, het aantal minuten sinds 00:00
    """
    minuten = time[0] * 60 + time[1]
    return minuten


def _time_to_int(bezoeken):  # redundant
    """
    Zet de bezoektijden om in minuten sinds 00:00 (beide de begin- en eindtijd)
    :param bezoeken: lijst van bezoeken, elk bezoek is een lijst met in volgorde: naam, nr, begintijd, eindtijd
    :return: None
    """
    for bezoek in bezoeken:
        bezoek[3] = _in_minuten(bezoek[3])
        bezoek[4] = _in_minuten(bezoek[4])

    # return niet nodig -> de lijsten worden aangepast en dus zal "bezoeken" al veranderd zijn.


# def start_bezoek(bezoeken):
#     """
#     Wie wordt eerst bezocht, gebaseerd op de vroegste en laatste mogelijke bezoektijd
#     :param bezoeken:
#     :return:
#     """
#     begintijd_bezoek = bezoeken[0][2]
#     eindtijd_bezoek = bezoeken[0][3]
#     eerste_bezoek = 0
#     bezoek_id = 0
#     for bezoek in bezoeken[1:]:
#         bezoek_id += 1
#         if bezoek[2] < begintijd_bezoek:
#             eerste_bezoek = bezoek_id
#         elif bezoek[2] == begintijd_bezoek and bezoek[3] < eindtijd_bezoek:
#             eerste_bezoek = bezoek_id
#
#     return eerste_bezoek


# TODO: Fix this goddamn mess
def mogelijke_bezoek_volgorde(rijtijden, bezoeken, tijd=0, vorig_bezoek=None):
    """
    Maakt een lijst aan, die een mogelijke bezoek volgorde is. Als er geen is, returnt dit None.

    :param rijtijden: Een matrix van rijtijden
    :param bezoeken: Een lijst van bezoeken
    :param tijd: de gepasseerde tijd, in minuten
    :param vorig_bezoek: het vorig bezoek, vanaf waar we moeten vertrekken
    :return: list met indexen van bezoeken, die een mogelijke bezoekvolgorde voorstelt]
    """

    # -- We loopen door elk te bezoeken bezoek en kijken of het mogelijk is er te geraken met de opgegeven tijd.
    # - Vanaf we een mogelijke volgorde hebben, slaan we die op en returnen we die.
    if len(bezoeken) == 1:
        if tijd > _in_minuten(bezoeken[0][4]):
            return None
        else:
            return bezoeken[0][0]

    for bezoek in bezoeken:
        nog_te_bezoeken = bezoeken.copy()
        nog_te_bezoeken.remove(bezoek)

        # Bij eerste iteratie: tijd is -1
        if vorig_bezoek is None:
            start_tijd = _in_minuten(bezoek[3])
            rest_volgorde = mogelijke_bezoek_volgorde(rijtijden, nog_te_bezoeken, start_tijd + 10, bezoek)
            if rest_volgorde is not None:
                return [bezoek[0]] + rest_volgorde
            else:
                continue

        # We krijgen een tijd mee => we moeten naar het volgende bezoek rijden en verliezen daardoor tijd
        else:
            rijtijd = rijtijden[bezoek[2]-1][vorig_bezoek[2]-1]
            aankomsttijd = rijtijd + tijd
            if aankomsttijd > _in_minuten(bezoek[4]):
                continue
            else:
                vroegste_tijd = max(aankomsttijd + 10, _in_minuten(bezoek[4]))
                rest_volgorde = mogelijke_bezoek_volgorde(rijtijden, nog_te_bezoeken, vroegste_tijd, bezoek)
                if rest_volgorde is not None:
                    return [bezoek[0]] + rest_volgorde
                else:
                    continue

    # We vinden nooit een mogelijke volgorde tijdens het doorlopen van alle mogelijkheden:
    # Return None.
    return None


def main():
    rijtijden = [( 0, 15, 20,  3),
                 (15,  0, 10, 10),
                 (20, 10,  0, 37),
                 ( 3, 10, 37,  0)]
    bezoeken = [[1, "Piet", 1, (9, 30), (10, 0)],
                [2, "Jan", 2, (9, 0), (10, 0)],
                [3, "Petra", 3, (10, 0), (10, 15)],
                [4, "Janis", 4, (9, 0), (10, 0)],
                [5, "Jan", 2, (11, 0), (11, 15)],
                [6, "Petra", 3, (11, 15), (11, 30)]]

    print(mogelijke_bezoek_volgorde(rijtijden, bezoeken))


main()
