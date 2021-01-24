# I originally had a factorial function, however,
# this takes a lot of computing time and is entirely unnecessary
#
# def fac(x):
#     # Result starts off as 1 for numbers 0 and 1
#     y = 1
#
#     # For numbers larger than 1, calculate
#     if x >= 2:
#         for i in range(1, x+1):
#             y *= i
#
#     return y

# e**x = SUM from n=0 to +oo for ( x**n / n! )


x_value = float(input("Enter the exponent x:\n> "))
n = 0
y_value = 0.0

# Initialise the n_fac variable = n!
n_fac = 1
# Initialise a separate case result for the equation (less calculation)
in_between = (x_value ** n / n_fac)


# Keep adding on to the sum until the difference is insignificant
while in_between > 0.000000000000001:
    y_value += in_between
    n += 1
    n_fac *= n
    in_between = (x_value ** n / n_fac)

# This means: print a string, but replace {} inside the string with a variable (the .format() part)
# I added extra info, so it fits my liking:
# 1. There should be some things to consider while changing the variable into a string (the ":" ), which are;
# 2. It should be considered a float (f)
# 3. It must have a maximum of 15 characters after the decimal point (.15)
# Example: let's say y_value == 23.345
# The string will then be: "23.345000000000000"
print("{:.15f}".format(y_value))
