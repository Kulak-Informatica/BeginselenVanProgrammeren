# These are literally the easiest goddamn functions I ever had to create.
# Goddamnit, kulak. Thought this was gonna be a challenge. You let me down.

# Dame dane
def swap(series):
    series[0], series[-1] = series[-1], series[0]
    return series


# dame yo dame na no yo
def shift(series):
    series = [series[-1]] + series[0:len(series)-1]
    return series


# anta ga suki de suki sugite
def replaceEvenWithZeros(series):
    replaced = []
    for num in series:
        if num % 2:
            replaced.append(num)
        else:
            replaced.append(0)
    return replaced


# dore dake tsuyoi osake de mo
def moveEvenToFront(series):
    even_at_front = [num for num in series if not num % 2] + [num for num in series if num % 2]
    # ... what? I need *some* sort of a challenge.
    return even_at_front


# yugamanai omoide ga
def reverse(series):
    return series[::-1]


# baka mitai...
def main():
    series = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19]
    print(swap(series))
    series = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19]
    print(shift(series))
    series = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19]
    print(replaceEvenWithZeros(series))
    series = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19]
    print(moveEvenToFront(series))
    series = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19]
    print(reverse(series))


# I didn't take this seriously at all.
main()
