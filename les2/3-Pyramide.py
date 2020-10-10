height = int(input("height: "))  # Input for height of pyramid

# Check to see if height is valid
if height > 0:

    # Create each layer of the pyramid
    for i in range(0, height):
        layer = " " * (height -1 -i)  # Spaces before the X's in a layer
        layer += "X" + "X" * 2 * i  # Add amount of X's in layer
        print(layer)

# if the height was not valid, notify:
else:
    print("Invalid number, please enter a number equal to or greater than 1.")
