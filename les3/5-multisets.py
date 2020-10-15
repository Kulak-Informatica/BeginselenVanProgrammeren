# Fixed it. Finally.
# Not my finest moment.

def union(set1, set2):
    uniset = dict(set1)

    for key, value in set2.items():
        if key in set1:
            uniset[key] += value
        else:
            uniset[key] = value

    return uniset


def intersection(set1, set2):
    interset = {}

    for key, value in set1.items():
        if key in set2:
            interset[key] = min(set2[key], value)

    return interset


def difference_set(set1, set2):
    diffset = dict(set1)

    for key, value in set2.items():
        if key in set1 and set1[key] > value:
            diffset[key] -= value
        elif key in set1:
            diffset.pop(key)

    return diffset


# Testing the functions:
set1 = {'appel': 3, 'banaan': 4}
set2 = {'peer': 2, 'banaan': 5}
print("set1 U set2 =", union(set1, set2))
print("set2 U set1 =", union(set2, set1))
print("set1 /\\ set2 =", intersection(set1, set2))  # double backslash needed to negate what a backslash would do
print("set2 /\\ set1 =", intersection(set2, set1))
print("set1 - set2 =", difference_set(set1, set2))
print("set2 - set1 =", difference_set(set2, set1))
