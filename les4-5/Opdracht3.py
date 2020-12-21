def convert(input):
    returnedValue = ""
    for i in range(len(input)):
        returnedValue += f"/* {1+i} */ {input[i]}\n"
    return returnedValue

def main():
    fileIn_name = input("> ") + ".txt"
    fileIn = open(fileIn_name, "r").read().split('\n')

    fileOut_name = input("> ") + ".txt"
    #fileOut_name = fileIn_name.replace("I", "O")

    fileOut = open(fileOut_name, "w")
    convertedTekst = convert(fileIn)
    fileOut.write(convertedTekst)

main()