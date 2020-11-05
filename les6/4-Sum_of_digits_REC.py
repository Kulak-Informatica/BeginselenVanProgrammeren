def sum_of_digits_rec(num):
    num = str(num)  # string of string won't give error
    if len(num) == 1:
        return int(num)
    return int(num[0]) + sum_of_digits_rec(num[1:])


def main():
    print(sum_of_digits_rec(55555))


main()
