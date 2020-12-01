def throw_dice(amount=20):
    from random import randint
    throws = []
    for i in range(amount):
        throws.append(randint(1, 6))
    return throws


def find_longest(values):
    # -- Indexes --
    # - The indexes that I use to keep up with where I'm at and where interesting series start
    start = 0  # start of longest series of equal numbers
    this_start = 0  # start of current series
    index = 1  # index of current digit

    # -- Length vars --
    # - variables to keep up with the length of the longest series and currently tested series
    length = 1  # length of longest series
    this_length = 1  # length of current series

    # We start our loop with the second number, and compare it to the previous.
    # I already adjusted variables for this case.
    last = values[0]
    for value in values[1:]:
        # if value same as last => current length +1
        if value == last:
            this_length += 1
            # if longest => start becomes current start
            if length < this_length:
                start = this_start
                length = this_length

        # if different value => current length = 1, current start = this index
        else:
            this_start = index
            this_length = 1

        index += 1
        last = value

    return start, length


# Here you find bad code. This code has to search for a certain index in the list twice,
# then runs through the entire list once, then runs through the entire list again, joining the elements
# and then it also has to search for 2 strings of code and replace both.
# It would be a lot simpler if I just run through the entire list once, check if I'm at a certain index,
# and add brackets on those indexes. Oh, and turn each element into a string *during* the loop.

# def stringify_list(non_string_list):
#     string_list = []
#     for element in non_string_list:
#         string_list.append(str(element))
#     return string_list
#
#
# def indicate(start, length, elements):
#     elements.insert(start, "(")
#     elements.insert(start + length + 1, ")")
#     elements = stringify_list(elements)
#     indicated = " ".join(elements).replace("( ", "(").replace(" )", ")")
#     return indicated

def indicate(start, length, elements):
    indicated_string = ""
    end = start + length - 1  # if start == end, then end == start + length (= +1) - 1
    last_index = len(elements) - 1  # the index of the last number
    i = 0  # Current index of the loop

    for element in elements:
        # the number we're at is the start of the longest: add an opening bracket
        if i == start:
            indicated_string += "("

        # add the number
        indicated_string += str(element)

        # the number we're at is the end of the longest: add a closing bracket
        if i == end:
            indicated_string += ")"

        # the number we're at is not the last: add a space between this number and the next
        if i != last_index:
            indicated_string += " "

        # update the index for the next number
        i += 1

    return indicated_string


def main():
    dice = throw_dice(20)  # if so desired, we can add an argument to throw_dice(amount) to change the amount of dice.
    start, length = find_longest(dice)
    print(indicate(start, length, dice))


main()
