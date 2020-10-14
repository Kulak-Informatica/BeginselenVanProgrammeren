# Given dictionary:
scoreAantallen = {"A":8, "B":13, "D":3, "F":2, "C":6}

# Opdracht a
print("Keys:", scoreAantallen.keys())
# Opdracht b
print("Values:", scoreAantallen.values())
# Opdracht c
print("Key-value pairs:", scoreAantallen.items())
# Opdracht d
print("Sorted key-value pairs:", sorted(scoreAantallen.items()))
# Opdracht e
for letter in sorted(scoreAantallen):
    print(letter + ": ", scoreAantallen[letter]*"*")  # type(letter) = str, type(scoreAantallen[letter]) = int
