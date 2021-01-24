total = int(input("Amount of seconds:  "))
print("converting to days, hours, minutes and seconds...")

seconds = total % 60
minutes = (total // 60) % 60
hours = (total // 60 // 60) % 24
days = total // 60 // 60 // 24

print("{} days, {} hours, {} minutes and {} seconds.".format(days, hours, minutes, seconds))
