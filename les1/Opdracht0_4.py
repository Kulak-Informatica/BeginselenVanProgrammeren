tijd = int(input("> "))

dagen = tijd // (24*60*60)
dagenRest = tijd % (24*60*60)

uren = dagenRest // (60*60)
urenRest = dagenRest % (60*60)

minuten = urenRest // 60
seconden = urenRest % 60

print(f"{dagen} dagen, {uren} uren, {minuten} minuten en {seconden} seconden.")