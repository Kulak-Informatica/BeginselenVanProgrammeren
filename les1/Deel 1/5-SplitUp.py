# Fuckers only asked for first and last 3,
# just spent 5 minutes trynna figure out how 2 split them up every three characters
# like this: input = "Biggie Cheese" => "Big...gie... Ch...ees...e"

string = input("string:\n> ")

# Stel len == 9: string[START:3] + "..." + string[6:END]
msg = string[:3] + "."*3 + string[-3:]

print(msg)
