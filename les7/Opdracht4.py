"""
def permutatie(lst):
   if len(lst) == 1:
     return [lst]

   permutaties = []
   for a in lst:
     overblijvende = [i for i in lst if i != a]
     sublist = permutatie(overblijvende)
     for b in sublist:
       permutaties.append([a] + b)

   return permutaties


lst = ["ik", "programmeer", "graag"]
print([f"{i[0]} {i[1]} {i[2]}" for i in permutatie(lst)])

"""

def genereerZinnen(woordenLijst):
    if len(woordenLijst) == 1:
        return [woordenLijst[0]]

    resultaten = []

    for woord in woordenLijst:
        restWoordenLijst = list(woordenLijst)
        restWoordenLijst.remove(woord)

        restZinnen = genereerZinnen(restWoordenLijst)

        for zin in restZinnen:
            resultaten.append(woord + " " + zin)

    return resultaten




def main():
    woorden = ["ik", "programmeer", "graag"]
    print(genereerZinnen(woorden))



main()

