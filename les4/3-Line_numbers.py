def add_line_number(text):
    text = text.split("\n")
    i = 1
    text_w_numbers = []
    for line in text:
        line = f"/* {i} */ " + line
        text_w_numbers.append(line)
        i += 1

    return "\n".join(text_w_numbers)


def main():
    text = "Hello!\nI am David.\nI am a student, and I am currently studying.\n"
    text += "Studying stands for \"student dying\". Please send help."

    print(add_line_number(text))


main()
