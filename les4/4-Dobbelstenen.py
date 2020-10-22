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


def stringify_list(non_string_list):
    string_list = []
    for element in non_string_list:
        string_list.append(str(element))
    return string_list


def indicate(start, length, elements):
    elements.insert(start, "(")
    elements.insert(start + length + 1, ")")
    elements = stringify_list(elements)
    indicated = " ".join(elements).replace("( ", "(").replace(" )", ")")
    return indicated


def main():
    dice = throw_dice()
    start, length = find_longest(dice)
    print(indicate(start, length, dice))


main()
