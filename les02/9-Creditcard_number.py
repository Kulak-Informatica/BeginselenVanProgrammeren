# Input of a string with numbers, with spaces
# Replacing each space in the string with an empty string results in one large string of only numbers
# Example: "1234 5678 1234 5670".replace(" ", "") ==  "12345678912345670"
# This means that any misplaced or unnecessary spaces will have no effect on the program
cardnumb = input("Please enter a valid card number.\nCard number: ").replace(" ", "")
is_number = False

# testing to see if the input is indeed a number:
while not is_number:
    try:  # This means we expect to potentially get an error
        h = int(cardnumb)  # if cardnumb is not a strict number, this will return a ValueError
    except ValueError:  # if a ValueError is found, do this instead:
        cardnumb = input("Invalid input. Try again:\nCard number: ")  # ask for another input
    else:  # if no errors were found in the try clause, continue. (separate to not catch any errors we didn't expect)
        is_number = True  # essentially: stop the while loop
        del h  # delete the help variable

# indicator to check if index of number is even or odd
even = True

# Initialize variable for total sum
total = 0

# Each digit in the number (Initially, type is str, reworked to int)
for digit in cardnumb:
    digit = int(digit)

    # When even index...
    if even:

        # When double digits, separate and add each to sum
        if digit >= 5:  # digit*2 >= 10  <=>  digit >= 5

            # Since the tested digit will always be smaller than 10, the double digit must be smaller than 20
            # That means the first digit will always be 1, and the second digit == 2*digit - 10
            # Therefore, digit1 + digit2 == (1) + (2*digit - 10)
            # == 2*digit + (1 - 10)  ==  2*digit - 9
            total += digit * 2 - 9

        # Else, simply add double
        else:
            total += digit * 2

    # When odd index...
    else:

        # Add digit to total sum, next index even
        total += digit
        index = 0

    # Next label will be even if previous is odd, and vice versa
    even = not even

# When the total sum is divisible by 10 => Valid number
# A simple way to show this is to print(not total % 10), which will show "True" if valid. Even better:
# print("Valid =", not total % 10)
# This works because integers can also be used as booleans: 0 is seen as False, all others (including negative) as True
# This would show "Valid = True" if valid.
# (I wanted to print some funny robot-like text instead, because, why not?)
if not total % 10:
    print("Valid number, continuing to monitor...")  # Subnautica reference
else:
    print("Invalid number, please try again in 99999 hours.")  # Subnautica reference
