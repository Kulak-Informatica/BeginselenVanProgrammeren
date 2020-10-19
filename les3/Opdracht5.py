set1 = {'appel': 3, 'banaan': 4}
set2 = {'peer': 2, 'banaan': 5}

#uni
def uni(set1, set2):
    merged = set1.copy()
    for k, v in set2.items():
        if k not in merged:
            merged[k] = v
        else:
            merged[k] += v
    return merged

def doorsn(set1, set2):
    merged = dict()
    for k, v in set1.items():
        if k in set2 and set2[k] <= v:
            merged[k] = set2[k]
        elif k in set2:
            merged[k] = v
    return merged

def verschil(set1, set2):
    merged = set1.copy()
    for k, v in set2.items():
        if k in set1:
            value = set1[k] - v
            if value > 0:
                merged[k] = value
            else:
                merged.pop(k)

    return merged

print(f"set1 = {set1}")
print(f"set2 = {set2}")
print(f"set1 U set2 = {uni(set1, set2)}")
print(f"set2 U set1 = {uni(set2, set1)}")
print(f"set1 /\ set2 = {doorsn(set1, set2)}")
print(f"set2 /\ set1 = {doorsn(set2, set1)}")
print(f"set1 - set2 = {verschil(set1, set2)}")
print(f"set2 - set1 = {verschil(set2, set1)}")