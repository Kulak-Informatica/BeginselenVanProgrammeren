# NOTE: never finished this.
# The dude's nuts... We got 3 hours, right? How are we ever supposed to WRITE all of this?

class Groentewinkel:
    def __init__(self):
        ...


class Klant:
    def __init__(self, naam, gekochte_producten):
        self._naam = naam
        self._gekochte_producten = gekochte_producten
        ...


class SporadischeKlant(Klant):
    """
    Sporadische klanten geven het minste informatie:
    We houden enkel bij hoeveel ze aankochten en bij welke datum.
    """
    def __init__(self, naam, gekochte_producten):
        super().__init__(naam, gekochte_producten)
        # Aanmaken dict: (datum -> aantal aankopen)
        ...

    def koop_producten(self, gekochte_producten):
        ...


class RegelmatigeKlant(Klant):
    def __init__(self, naam, gekochte_producten):
        super().__init__(naam, gekochte_producten)
        # Aanmaken dict: (categorie -> dict: (datum -> aantal aankopen))
        ...

    def koop_producten(self, gekochte_producten):
        ...


class ProfessioneleKlant(RegelmatigeKlant):  # prof. klanten zijn ook regelmatige klanten, maar met meer informatie.
    def __init__(self, naam, gekochte_producten):
        super().__init__(naam, gekochte_producten)
        # Aanmaken dict: (Product -> aantal toekomstige aankopen)
        ...


class Product:
    def __init__(self):
        ...


class SeizoensGroenten(Product):
    def __init__(self):
        super().__init__()
        ...


class IngevoerdeGroenten(Product):
    def __init__(self):
        super().__init__()
        ...


class Fruit(Product):
    def __init__(self):
        super().__init__()
        ...
