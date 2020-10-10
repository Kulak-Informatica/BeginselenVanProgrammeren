year = int(input("year: "))

if (not year % 100 == 0 and year % 4 == 0) or (year % 400 == 0):
    print(year, "is een schrikkeljaar.")
else:
    print(year, "is geen schrikkeljaar.")