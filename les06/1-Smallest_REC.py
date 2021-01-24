def smallest_rec(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], smallest_rec(lst[1:]))


def main():
    print(smallest_rec([6, 3, 4, 1, 8.0, 27, -5, 3]))


main()
