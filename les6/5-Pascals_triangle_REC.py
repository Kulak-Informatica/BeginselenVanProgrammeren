def pascals_triangle(height):
    if height == 1:
        return [[1]]
    if height == 2:
        return pascals_triangle(1) + [[1, 1]]

    # -- Generate the top lines
    triangle_top = pascals_triangle(height - 1)

    # -- Extract the last line
    triangle_last = triangle_top[-1]

    # -- Based on the previous line, create the next line
    # Every element is the sum of the element "above" and the element "above to the left"
    # The exceptions are the ones on the ends, since there is either no above or above to the left. These are ones. So:

    # - Every element starting from the second (i=1) is the sum of "above" (i) and "above left" (i-1)
    pascal_line = [1]
    for i in range(1, height-1):
        pascal_line.append(triangle_last[i-1] + triangle_last[i])
    pascal_line.append(1)

    # -- Add the new line to the previously generated triangle top, and return.
    triangle_top.append(pascal_line)
    return triangle_top


# I also want to try it out linearly. As a challenge.
def pascals_triangle_lin(height):
    if height == 0:
        return []
    elif height == 1:
        return [[1]]

    triangle = [[1], [1, 1]]
    # The next comment (on line 39) has been added automatically: PyCharm thinks the line after has no effect, this
    # disables the check which causes that. (Side note: that line does have effect)

    # noinspection PyStatementEffect
    [triangle := triangle + [[1]+[triangle[-1][i-1] + triangle[-1][i] for i in range(1, size)]+[1]] for size in range(2, height+1)]

    # Holy shit this is a mess. Let me try to explain what I did:
    # I decided to attempt to make the code in as few lines of actual code as possible.
    # I'm using "list comprehension" (eg. [x**2 for x in range(5)] -> [0, 1, 4, 9, 16]) to create a list for the new row
    # That list comprehension is INSIDE another list comprehension, which uses some black magic to work.
    # Essentially, I reassign my variable "triangle" every iteration of this outer list comprehension.
    # I do that by using the walrus operator := (because it looks like a walrus)
    # The walrus operation works just like the normal assignment operator (eg. a = 5), but you can use it in-line.
    # So, for size in range(2, height+1) I reassign triangle to the triangle + the new created line.

    return triangle


def triangle_printer(triangle: list):
    for line_list in triangle:
        # Initiate string, to display each number on one line
        line_string = ""

        # add each element to string
        for el in line_list:
            line_string += str(el) + " "

        print(line_string.strip(" "))


def main():
    triangle_printer(pascals_triangle_lin(7))
    # print(pascals_triangle_lin(7))


# Apparently if you import code, it will also run the code (which makes sense, since you define all functions by
# running the code itself.)
# Doing this checks if the code is being imported or not, by checking if the location it is run from is just "main", or
# if it's from an imported file (in which case it'll give the name of the imported file.)
# Not useful here, but decided to add it either way.
if __name__ == "__main__":
    main()
