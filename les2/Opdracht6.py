from math import *

def is_priem(num):
    if(num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    return False

invoer = int(input("> "))

for i in range(invoer):
    if is_priem(i):
        print(i)
