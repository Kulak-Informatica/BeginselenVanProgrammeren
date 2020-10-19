scoreAantallen = {"A":8, "B":13, "D":3, "F":2, "C":6}

for i in scoreAantallen.keys():
    print(i, end=" ")

print()

for i in scoreAantallen:
    print(scoreAantallen[i], end=" ")

print()
list = [(k, v) for k, v in scoreAantallen.items()]
print(list)

sortedlist = sorted(list)
print(sortedlist)

for i in sortedlist:
    print(f"{i[0]}: {'*'*i[1]}")