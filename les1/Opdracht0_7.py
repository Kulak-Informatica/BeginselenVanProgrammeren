num1 = int(input("> "))
num2 = int(input("> "))

som = num1 + num2
verschil = num1 - num2
afstand = abs(verschil)
product = num1 * num2
gemiddelde = som/2
max = max(num1, num2)
min = min(num1, num2)

print('{:>12} {:^10}'.format("Som:", som))
print('{:>12} {:^10}'.format("Verschil:", verschil))
print('{:>12} {:^10}'.format("Afstand:", afstand))
print('{:>12} {:^10}'.format("Product:", product))
print('{:>12} {:^10}'.format("Gemiddelde:", gemiddelde))
print('{:>12} {:^10}'.format("Maximum:", max))
print('{:>12} {:^10}'.format("Minimum:", min))