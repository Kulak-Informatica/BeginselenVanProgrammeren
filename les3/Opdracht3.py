set1 = set(range(1, 11))
set2 = set(range(10, 30))
set3 = set(range(5, 20))

newset = set()
for i in set1:
    newset.add(i)
for i in set2:
    if i not in newset:
        newset.add(i)
print(newset)

newset = set()
globset1 = set1.union(set2)
globset = globset1.union(set3)
for i in globset:
    if i in set1 and i not in set2 and i not in set3:
        newset.add(i)
    elif i not in set1 and i in set2 and i not in set3:
        newset.add(i)
    elif i not in set1 and i not in set2 and i in set3:
        newset.add(i)
print(newset)

newset = set()
globset1 = set1.union(set2)
globset = globset1.union(set3)
for i in globset:
    if i in set1 and i in set2 and i not in set3:
        newset.add(i)
    elif i not in set1 and i in set2 and i in set3:
        newset.add(i)
    elif i  in set1 and i not in set2 and i in set3:
        newset.add(i)
print(newset)
