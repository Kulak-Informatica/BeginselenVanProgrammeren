def next_value(value):
    if value % 2:
        result = 3 * value + 1
    else:
        result = value // 2
    return result


start = int(input("number from 1 and 100000\n?> "))

if 0 < start <= 1000000:
    # Initialising every variable
    result = start
    total = start
    max_num = start
    step = 0

    while result != 1:
        next_num = next_value(result)  # calculates next number in series
        max_num = max(max_num, result)  # calculates the maximum so far
        total += next_num  # keeps track of the total sum
        step += 1  # keeps track of the counter
        result = next_num  # assigns the last value to result, so we can loop once more

    average = total / (step+1)  # start value has step 0, so amount is step+1

    print("Starting value:  {:10d}".format(start))
    print("Steps:           {:10d}".format(step))
    print("Maximum:         {:10d}".format(max_num))
    print("Average:         {:13.2f}".format(average))
else:
    print("Invalid value, please enter a number from 1 to 1000000")