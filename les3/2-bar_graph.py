# Given:    - all inputs are positive numbers.
#           - Largest number must be represented by 40 *

# -- Inputting values --
# My idea of doing this is to let the user first input a series of numbers,
# separated by spaces, and using the str.split method to create a list:

values = input("Series of numbers, separated using spaces\n?>  ")  # \n stands for a newline
values = values.split(" ")  # splits a string between all spaces into a list of *(sub)strings* (!not ints or floats!)
values = [float(i) for i in values]  # converting all elements to floats

max_value = max(values)

# -- Printing the bars --
for value in values:
    # we might be able to use //, but I don't trust that it'll print the same values for small floats (<1)
    print(int(value/max_value * 40) * "*")
