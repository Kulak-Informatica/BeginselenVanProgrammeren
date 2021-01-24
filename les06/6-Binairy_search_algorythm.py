# extra challenge: instead of taking half every time, and searching from there, take a random guess in the list, and
# search from there
def search(lst, num):
    print(lst)
    length = len(lst)
    if (length == 1 and lst[0] != num) or length == 0:  # the list is empty or the only number isn't our number
        return False

    # as long as we're still searching for the number, take a guess where the number might be
    from random import randint
    index = randint(0, length - 1)
    guess = lst[index]
    if guess == num:
        return True  # the number is inside the list
    if num < guess:  # the number might be before our guess, so search from index 0 up till our index
        return search(lst[:index], num)

    # the number isn't the index, and before, so it might be after our index till the end
    # Why index and not index+1? If index is last element, lst[index+1:] gives error
    return search(lst[index:], num)


def main():
    from random import randint
    lst = []
    for i in range(1000):
        lst.append(randint(0, 10000))
    lst.sort()
    print(search(lst, 666))
    print(666 in lst)


main()
