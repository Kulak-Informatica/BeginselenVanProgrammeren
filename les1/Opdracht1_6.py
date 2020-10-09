import time


t1 = input("> ").split(":")
t2 = input("> ").split(":")

if int(t1[0]) >= 24 or int(t2[0]) >= 24 or int(t1[1]) >= 60 or int(t2[1]) >= 60:
    print("Geen geldig tijdsformaat")
else:
    tijd1 = int(t1[0])*60 + int(t1[1])
    tijd2 = int(t2[0])*60 + int(t2[1])

    verschil = abs(tijd2-tijd1)

    uren = verschil // 60
    minuten = verschil % 60

    if uren < 10:
        uren = "0"+str(uren)
    if minuten < 10:
        minuten = "0"+str(minuten)


    print(f"Het verschil is: {uren}:{minuten}")