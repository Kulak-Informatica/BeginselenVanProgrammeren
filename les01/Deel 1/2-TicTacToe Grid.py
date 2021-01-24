if "y" in input("Standard (Y/N)?  ").lower():
    columns, rows = 3, 3
else:
    columns = int(input("amount of columns: "))
    rows = int(input("amount of rows: "))

end = "+--" * columns + "+"
in_between = "|  " * columns + "|"

print(end)

for i in range(0, rows):
    print(in_between)
    print(end)
