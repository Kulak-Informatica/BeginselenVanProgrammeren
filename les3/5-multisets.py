# -- Union --
def union(set1, set2):
    for key, value in set2.items():
        if key in set1:  # If a key from set2 in set1: add numbers.
            set1[key] += value

        else:  # Else: add new key, assign the value.
            set1[key] = value

        return set1


# WIP -- Not complete yet, doing some stupid shit
def difference(set1, set2):

    for key, value in set1.items():
        # If the key is in set 2, and the result of the values of the key is greater than 0
        if key in set2 and value - set2[key] > 0:
            set1[key] -= set2[key]
        # Otherwise, simply add the key and value from set1
        elif key not in set2:
            set1.pop(key)

        return set1


def intersection(set1, set2):
    # For this one, I'm creating a new set, and adding all keys that are in both, assigning the minimum value.
    interset = {}
    for key, value in set1.items():

        # For each key in 1 that is in 2, interset[key] will have the lowest value from set1 and set2 for that key
        if key in set2:
            interset[key] = min(value, set2[key])

    return interset


# Testing the functions:
set1 = {'appel': 3, 'banaan': 4}
set2 = {'peer': 2, 'banaan': 5}
print("set1 U set2 =", union(set1, set2))
print("set2 U set1 =", union(set2, set1))
print("set1 /\\ set2 =", intersection(set1, set2))  # double backslash needed to negate what a backslash would do
print("set2 /\\ set1 =", intersection(set2, set1))
print("set1 - set2 =", difference(set1, set2))
print("set2 - set1 =", difference(set2, set1))