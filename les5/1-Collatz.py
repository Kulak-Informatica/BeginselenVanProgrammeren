# Since actually printing 1000000 values seems a bit overboard,
# I'm assuming we're supposed to be able to input a value from 1 to 1000000.
# The console isn't even large enough to actually hold 1000000 outputs, only a little less than 20000.
# However, just in case, I added both options.
# The calculations will happen as a function, so I don't have to type the same code twice.
def next_value(value):
    if value % 2:
        result = 3 * value + 1
    else:
        result = value // 2
    return result


def collatz(start):
    # Initialising every variable

    # 3 lines in one, definitely a good idea
    result = total = max_num = start
    step = 0

    while result != 1:
        next_num = next_value(result)  # calculates next number in series
        max_num = max(max_num, result)  # calculates the maximum so far
        total += next_num  # keeps track of the total sum
        step += 1  # keeps track of the counter
        result = next_num  # assigns the last value to result, so we can loop once more

    average = total / (step + 1)  # start value has step 0, so amount is step+1
    return step, max_num, average


print("You can choose to input a value from 1 to 1000000, or print all values.")
print("Input a value [1-1000000] or print all values [V]")
start = input("?> ")

# Testing to see if the input is viable to be a set as an integer
# This is new shit. Good shit. But new shit. So here's how this shit goes down:
# First, the try clause is executed. If an "exception" occurs, an error during the execution of a program,
# the rest of the clause is skipped, and we move on to the except clause. If the error type is the same as listed
# in the exception, it will execute the except clause. Otherwise, execution of the program stops as it is considered
# an "unhandled exception". What does that mean? I have no darn clue, but this /should/ work.
# Why not just test if every character is a number? That's lame. Also, if we were to work with bigger numbers,
# the time it'd take to test every digit goes up drastically. Probably. I actually have no clue. But who cares?
# This shit works, it looks cool, and it's new. Sounds like some good shit to use in my program.
try:
    int(start)  # if start is not a number, we get a ValueError and we move to "except"
    start_is_integer = True
except ValueError:
    start_is_integer = False

# if start not integer, ask to be sure, then execute the program.
if not start_is_integer and "y" in input("Are you sure you want to test all 1000000? [Y/N] ").lower():

    # Idea: keep track of the largest number, the largest step, and the largest average. Sounds fun.
    # So, here I set a few variables to test those things:
    max_of_max = [1, 1]
    max_average = [1, 1]
    max_step = [0, 1]
    for i in range(1, 1000001):
        # The actual program:
        step, max_num, average = collatz(i)
        print(f"STRT: {i:13d} | STP: {step:13d} | MAX: {max_num:13d} | AVG: {average:13.3f}")

        # The fun idea:
        max_step[0] = max(max_step[0], step)  # largest amount of steps needed and for which value
        if max_step[0] == step:
            max_step[1] = i
        max_average[0] = max(max_average[0], average)
        if max_average[0] == average:
            max_average[1] = i
        max_of_max[0] = max(max_of_max[0], max_num)
        if max_of_max[0] == max_num:
            max_of_max[1] = i

    print(f"Largest amount of steps: {max_step[0]}")
    print(f"Reached at: {max_step[1]}")
    print(f"Largest number reached in: {max_of_max[0]}")
    print(f"Reached at: {max_of_max[1]}")
    print(f"Largest average reached in: {max_average[0]}")
    print(f"Reached at: {max_average[1]}")

# if start an integer, execute for one value
elif start_is_integer and 0 < int(start) <= 1000000:
    step, max_num, average = collatz(int(start))
    print(f"Starting value:  {int(start):10d}")
    print(f"Steps:           {step:10d}")
    print(f"Maximum:         {max_num:10d}")
    print(f"Average:         {average:13.2f}")

# if start was an integer, but an invalid one, display message
elif start_is_integer:
    print("Invalid value, please enter a number from 1 to 1000000")
