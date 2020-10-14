# Since I don't have actual inputs (strings), I decided to create functions instead.
# The arguments for the function can then be actual sets.
# If I do need to add inputs, I simply have to transform the input strings to sets, apply these functions and print.

def symmetric_difference(set1, set2):
    # -- Operations I will use --
    #
    # set_a.difference(set_b) : returns a set containing all elements (el) in set_a that aren't in set_b
    # set_a.union(set_b) : returns the combination of both sets.
    #
    # -- Thought process --
    # First, I create a set with all el in 1 that aren't in 2:
    # set_result = set1.difference(set2)
    # eg. 1 = {1, 2, 3} || 2 = {3, 4, 5} || result1 = {1, 2}
    #
    # Then, I create a set with all el in 2 that aren't in 1:
    # set_result_2 = set2.difference(set1)
    # eg. 1 = {1, 2, 3} || 2 = {3, 4, 5} || result2 = {4, 5}
    #
    # Afterwards, I simply add the two together using the union:
    # set_result = set_result.union(set_result_2)
    # eg. result1 = {1, 2} || result2 = {4, 5} || result_total = {1, 2, 4, 5}
    #
    # Then, I return the result.
    # This is so simple I'll do this all in one line, however.
    return set1.difference(set2).union(set2.difference(set1))


def one_of_three(set1, set2, set3):
    # I can use the previous function to create the symmetric difference between set1 and set2.
    # That set will have all numbers that appear only once in both set1 and set2.
    # This means I can use the same function on this new set and set3 to get the result I want.
    set_h = symmetric_difference(set1, set2)
    return symmetric_difference(set_h, set3)


def two_of_three(set1, set2, set3):
    # I highly recommend drawing a venn diagram for this:
    # What we want is each intersection between the three circles,
    # without the center bit where all 3 intersect.
    # We COULD use the union of all 3 \ the function above of all three \ the intersection of all three
    # However, I'm planning on adding each intersection and removing the intersection of all three
    intersec12 = set1.intersection(set2)
    intersec13 = set1.intersection(set3)
    intersec23 = set2.intersection(set3)
    intersec123 = intersec12.intersection(set3)
    all_intersec = intersec12.union(intersec13.union(intersec23))
    return all_intersec.difference(intersec123)


# Here I'll print a few sets to test if what I'm doing is correct.
# NOTE: these variables may have different names from what's in the functions.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {3, 5, 6, 7}  # Added a three so there's a number which is in all sets

# function 1 -- Expected result: {1, 2, 4, 5}
func1 = symmetric_difference(set1, set2)
print(func1)

# function 2 -- Expected result: {1, 2, 4, 6, 7}
func2 = one_of_three(set1, set2, set3)
print(func2)

# function 3 -- Expected result: {5}
func3 = two_of_three(set1, set2, set3)
print(func3)