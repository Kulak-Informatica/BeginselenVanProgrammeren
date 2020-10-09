from math import *

x = float(input("> "))
y = float(input("> "))
r = sqrt((x**2) + (y**2))
angle = atan(x/y) * (180/pi)
print(f"r = {r}")
print(f"theta = {angle}")

