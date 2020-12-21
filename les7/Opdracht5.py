
##  Genereert zinnen volgens een gegeven skelet met woorden uit een gegeven dictionary
#   @param woordenDict
#   @param skelet
#   @return: een lijst met mogelijke zinnen
#
def genereerZinnen(woordenDict, zinSkelet):
    # Triviaal geval: een leeg skelet, oftewel een lege lijst.
    if len(zinSkelet) == 0:
        return ["."]  # Laatste karakter van de zin: het leesteken
    else:
        # Verklein probleem: genereer alle zinnen voor een kleiner zinSkelet
        kleinerZinSkelet = zinSkelet[1:]
        alleZinnenVoorKleinerSkelet = genereerZinnen(woordenDict, kleinerZinSkelet)

        # Samenvoegen: alle mogelijkheden voor het volledig skelet maken
        resultaat = []
        woordsoort = zinSkelet[0]  # gevraagde woordsoort voor de huidige locatie
        for key in woordenDict.keys():
            if woordenDict[key] == woordsoort:
                for zin in alleZinnenVoorKleinerSkelet:
                    resultaat.append(key + " " + zin)  # Zin uitbreiden met nieuwe woord
                                                       # en toevoegen aan resultaat

        return resultaat



