# Since I don't have actual inputs (strings), I decided to create functions instead.
# The arguments for the function can then be actual sets.
# If I do need to add inputs, I simply have to transform the input strings to sets, apply these functions and print.

def difference_of_sets(set1, set2):
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
    # Then, I simply return the result.
    # I'll do this all in one line, however.
    return set1.difference(set2).union(set2.difference(set1))

