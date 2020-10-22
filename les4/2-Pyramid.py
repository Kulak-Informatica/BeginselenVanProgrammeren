# I can literally just copy the code from lesson one, and just adjust a few minor things.

def pyramid(height, symbol="#"):
    if height > 0:

        # Create each layer of the pyramid
        for i in range(0, height):
            layer = " " * (height - 1 - i)  # Spaces before the symbols in a layer
            layer += symbol * (2 * i + 1)  # Add amount of symbols in layer
            print(layer)


def main():
    height = int(input("Enter the height of the pyramid:\n> "))
    while height < 1:
        height = int(input("Please enter a valid height:\n> "))
    symbol = input("Please enter the symbol used for the pyramid, or NONE if default should be used:\n> ")

    if len(symbol) > 1:
        pyramid(height)
    else:
        pyramid(height, symbol)

    print("=" * (height * 2 - 1))  # foundation of the pyramid. Otherwise it'll fall apart.


main()
