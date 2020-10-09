teken = "+"
invoer = int(input("> "))
som = 0

while invoer != 0:
    if teken=="+":
        som += invoer
        teken = "-"
    else:
        som -= invoer
        teken = "+"
    invoer = int(input("> "))

print(f"De som is {som}")