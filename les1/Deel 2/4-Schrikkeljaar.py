year = int(input("jaar:\n> "))

# if an integer is 0, it is considered the same as "False". Any other number is considered "True"
# this means we can write "is it divisible by 4?" as "is the rest, after division by 4, not 0?"
# example: year = 4 --> year % 4 (== 0 == False) --> not year % 4 (== True)
if year % 100 and not year % 4 or not year % 400:
    print(year, "is een schrikkeljaar.")
else:
    print(year, "is geen schrikkeljaar.")
