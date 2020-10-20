def pyramide(hoogte, symbol):
    string = ""
    for i in range(hoogte):
        string += ' '*(hoogte-i-1) + symbol*(2*i+1) + "\n"
    return string


def main():
    h = int(input("> "))
    s = input("> ")
    if s == "":
        s = "#"
    p = pyramide(h, s)
    print(p)

main()