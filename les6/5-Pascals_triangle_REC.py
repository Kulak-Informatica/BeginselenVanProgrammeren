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


def triangle_printer(pascals_triangle : list):
    for line_list in pascals_triangle:
        # Initiate string, to display each number on one line
        line_string = ""

        # add each element to string
        for el in line_list:
            line_string += str(el) + " "

        print(line_string.strip(" "))


def main():
    triangle_printer(pascals_triangle(7))


main()
