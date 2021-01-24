numb = int(input("Enter a positive integer: "))
prime = True

for i in range(2, numb//2 + 1):
    if numb % i == 0:
        print("{} is not a prime number.".format(numb))
        prime = False
        break

if prime:
    print("{} is a prime number.".format(numb))
