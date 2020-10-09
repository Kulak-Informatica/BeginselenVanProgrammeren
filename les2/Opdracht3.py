def pyramide(hoogte):
    for i in range(hoogte):
        print(' '*(hoogte-i-1) + 'X'*(2*i+1))


hoogte = int(input("> "))
pyramide(hoogte)