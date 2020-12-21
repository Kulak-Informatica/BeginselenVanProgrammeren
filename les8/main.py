from auto import Auto
from geometrie import *
from examens import *

## Hoofdprogramma
def main():

    # Auto
    mini = Auto(4.5)
    mini.tank(40)
    mini.rij(50)
    print(mini.getTankinhoud())

    # Cirkel
    cirkel = Cirkel(10)
    print("De straal van de cirkel:",cirkel.getStraal())
    print("De omtrek van de cirkel:",cirkel.berekenOmtrek())
    print("De oppervlakte van de cirkel:",cirkel.berekenOppervlakte())

    cilinder = Cilinder(5,10)
    print("De oppervlakte van de cilinder:",cilinder.berekenOppervlakte())
    print("De inhoud van de cilinder:",cilinder.berekenVolume())

    # Examens
    igor = Student("Igor","Wauters")

    bvp = Vak("Beginselen van Programmeren",6,0.2)
    exBvp = Examen(bvp,5,13)
    print("Het examen voor BVP heeft een totale score van",exBvp.berekenScore())
    igor.addExamen(exBvp)

    filo = Vak("Filosofie",3,0.9)
    exFilo = Examen(filo,9,13)
    print("Het examen voor Filo heeft een totale score van",exFilo.berekenScore())
    igor.addExamen(exFilo)

    print("De totale score van "+igor.getVoornaam()+" is: "+str(round(igor.getTotaleScore(),2))+" procent.")


# start de main
main()