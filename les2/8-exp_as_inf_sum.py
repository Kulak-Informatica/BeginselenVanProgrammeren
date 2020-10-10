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


x_value = float(input("Enter a number x:\n? "))
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

print("{:.15f}".format(y_value))
