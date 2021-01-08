def throw_dice(amount=20):
    from random import randint

    # -= UPDATED =-
    # Previously, this was the code I used to make the list:
    #
    # throws = []
    # for i in range(amount):
    #     throws.append(randint(1, 6))
    # return throws

    # However, we can use list comprehension to shorten all of this to one line, all because:
    # - We create a new list
    # - The elements in the list are added through the use of a for loop
    # - The elements are a simple and can be written using a few (here: 1) functions or other operations

    return [randint(1, 6) for _ in range(amount)]  # "_" used to indicate a throwaway variable (i.e. we don't use it)


def find_longest(values):
    # -= Reasoning =-

    # How would I do this?
    # We're given a list of elements, and we need to find the longest series of repeating elements in it.
    # In order to do that, we need to run through the elements one by one, and compare them to the previous.
    # During the loop, we can keep track of the elements we've seen, but we can't know what lies ahead, and if there
    # might be a longer series than we've found so far.
    # Therefore, we need to use 2 sets of variables, which I'll call "the runners" and "the (data)bank"

    # -= The Runners =-
    # Essentially, the runners are only important during the loop. Every "series" they find, they keep track of these:
    # - Where did this series start?
    # - How long is the series right now?
    # This happens during the for loop, and resets with every "new" series (everytime a different number is found)
    # That is why I've named all my "runner variables" to start with "this_"

    # -= The Databank =-
    # These keep track of the values we might be interested in. If we found a series with length 3, the runners might
    # find more series with length of 4 or more, but until they do, we can't say for certain if there's a longer series.
    # That's why the databank exists: up until this point, what's the longest series the runners found?
    # At the end of the loop or the end of the list, these will be the variables that we we're looking for.
    # Because these are the "important" variables, I've given them simple names, such as "start" and "length"

    # -= The Code =-

    # -- Index vars --
    # - The indexes that I use to keep up with where I'm at and where an interesting series start
    start = 0  # start of longest series of equal numbers (DATABANK)
    this_start = 0  # start of current series (RUNNER)
    index = 1  # index of current digit (Technically runner as well)

    # -- Length vars --
    # - variables to keep up with the length of the longest series and currently tested series
    length = 1  # length of longest series (DATABANK)
    this_length = 1  # length of current series (RUNNER)

    # We start our loop with the second number, and compare each number to the previous.
    # That's why i've set index and the lengths to 1 instead of 0
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
#     indicated = " ".join(elements).replace("( ", "(").replace(" )", ")")  # str.join might be faster than I thought
#     return indicated

def indicate(start, length, elements):
    indicated_string = ""
    end = start + length - 1  # Reasoning: say start 0 and length 1, end has to be 0 as well. That's why I subtract 1
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
