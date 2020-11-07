# I want it to be purely one recursive function, but I can't really think of how to do it...
# EDIT: Easily done using a default value which asks if we just take the sum or not. Feels like cheating tho.
def average_rec(lst, sum_up=False):
    resulting_sum = lst[0]
    if len(lst) == 1:
        return resulting_sum  # The average of a list of length 1 is equal to the 1 element in it

    # if we read this code, the length is greater than 1. We must take the sum of the elements in the list, recursively.
    resulting_sum += average_rec(lst[1:], True)  # take the rest of the list, but only count them up

    if not sum_up:  # if this is false, this is the first iteration of this code, so we divide by the length of lst
        resulting_sum /= len(lst)

    return resulting_sum


def main():
    from random import randint

    lst = [randint(0, 10) for i in range(0, 100)]

    print(lst)
    print(sum(lst))
    print(len(lst))
    print(average_rec(lst))


main()
