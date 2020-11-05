def palindrome_rec(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    return True and palindrome_rec(string[1:-1])


def main():
    print(palindrome_rec("HelloolleH"))  # I know words like kayak and lepel are palindromes, leave me be


main()
