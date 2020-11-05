def mergesort(lst):
    if len(lst) == 1:
        return lst
    center = len(lst)//2  # return center index (2 if len 4; 1 if len 3) to split up
    left = mergesort(lst[:center])  # say len 4: center = 2, split up in 0, 1 and 2, 3
    right = mergesort(lst[center:])  # say len 3: center = 1, split up in 0 and 1, 2
    # if len = 2, center is 1, split up in 0 and 1, length of lists = 1, returns lists themselves

    sortedlst = []
    # Need to fill this in, will do this later

    return sortedlst


def main():
    from random import randint
    _ = []
    for i in range(50):
        _.append(randint(0, 1000))

    print(mergesort(_))


main()
