# I can literally just copy the code from lesson one, and just adjust a few minor things.
# UPDATE: After digging through the formatting of strings, I figured out I could just
# format the string so the "building blocks" become centered in a string with length (height * 2 + 1)
# This is possible with the str.format() method, but not using the "%s" %(data) method.

# def pyramid(height, symbol="#"):
#     if height > 0:
#
#         # Create each layer of the pyramid
#         for i in range(0, height):
#             layer = " " * (height - 1 - i)  # Spaces before the symbols in a layer
#             layer += symbol * (2 * i + 1)  # Add amount of symbols in layer
#             print(layer)

def pyramid(height, symbol="#"):
    if height > 0:

        # Create each layer of the pyramid
        for i in range(0, height):
            # layer = "{:^{}}".format(symbol*(1+2*i), 2*height-1)
            layer = f"{symbol*(1+2*i):^{2*height-1}}"  # equivalent to the method above
            print(layer)


# The actual new code:
def main():
    height = int(input("Enter the height of the pyramid:\n> "))
    while height < 1:
        height = int(input("Please enter a valid height:\n> "))
    symbol = input("Please enter the symbol used for the pyramid, or NONE if default should be used:\n> ")

    if len(symbol) > 1 or len(symbol) == 0:
        pyramid(height)
    else:
        pyramid(height, symbol)

    print("=" * (height * 2 - 1))  # foundation of the pyramid. Otherwise it'll fall apart.


main()
