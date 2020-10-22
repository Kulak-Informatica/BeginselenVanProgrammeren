def add_line_numbers_txt(text):
    text = text.split("\n")
    i = 1
    text_w_numbers = []
    for line in text:
        line = f"/* {i} */ " + line
        text_w_numbers.append(line)
        i += 1

    return "\n".join(text_w_numbers)


def add_line_numbers(inputfile, outputfile):
    with open(inputfile) as file:
        text = file.read()
    file.close()

    text = add_line_numbers_txt(text)

    with open(outputfile, "w") as file:
        file.write(text)
    file.close()


def main():
    inputfile = input("Name of input:\n> ")
    outputfile = input("Name of output:\n> ")
    # text = "Hello!\nI am David.\nI am a student, and I am currently studying.\n"
    # text += "Studying stands for \"student dying\". Please send help."

    add_line_numbers(inputfile, outputfile)

    print("Line numbers added.")


main()
