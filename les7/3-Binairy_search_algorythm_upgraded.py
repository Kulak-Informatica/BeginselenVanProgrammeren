def binairy_search(lst, num, start=0, end=-1):
    if len(lst) == 1 and lst[0] == num:
        return True
    elif len(lst) == 1:
        return False

    # Length of list does not equal one if this point is reached

    # Initial run of function: set end to length - 1 of lst
    if end == -1:
        end = len(lst) - 1

    center = (start + end) // 2
    guess = lst[center]
    if guess == num:
        return True
    elif num < guess:
        return binairy_search(lst, num, start, center)

    return binairy_search(lst, num, center, end)


def main():
    from random import randint
    import time

    for i in range(2, 5):

        lst = []
        for _ in range(500):
            lst.append(randint(0, 3**i))

        lst.sort()

        starttime = time.perf_counter()

        print(binairy_search(lst, 7))

        endtime = time.perf_counter()

        total_time = endtime - starttime

        print(total_time)


main()
