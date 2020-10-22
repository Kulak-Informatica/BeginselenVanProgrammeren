def throw_dice(amount=20):
    from random import randint
    throws = []
    for i in range(amount):
        throws.append(randint(1, 6))
    return throws


def find_longest(values):
    # -- Indexes --
    start = 0  # start of longest series
    this_start = 0  # start of current series
    index = 1  # index of current digit

    # -- Length vars --
    length = 1  # length of longest series
    this_length = 1  # length of current series

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
    die = throw_dice()
    start, length = find_longest(die)
    print(indicate(start, length, die))


main()
