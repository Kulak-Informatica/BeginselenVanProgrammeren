def mergesort(lst):
    if len(lst) == 1:
        return lst

    center = len(lst)//2  # return center index (2 if len 4; 1 if len 3) to split up
    left = mergesort(lst[:center])  # say len 4: center = 2, split up in 0, 1 and 2, 3
    right = mergesort(lst[center:])  # say len 3: center = 1, split up in 0 and 1, 2
    # if len = 2, center is 1, split up in 0 and 1, length of lists = 1, returns lists themselves

    sortedlst = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sortedlst.append(left[i])
            i += 1
        else:
            sortedlst.append(right[j])
            j += 1

    if i < len(left):
        sortedlst.extend(left[i:])
    elif j < len(right):
        sortedlst.extend(right[j:])

    return sortedlst


def main():
    from random import randint
    _ = []
    for i in range(50):
        _.append(randint(0, 1000))

    mergesorted = mergesort(_)
    print(mergesorted)
    _.sort()
    print(mergesorted == _)


main()
