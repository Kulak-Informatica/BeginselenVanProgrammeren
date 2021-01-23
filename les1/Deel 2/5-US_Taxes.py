def tax_divider(newtax):
    tax_per_amount = [newtax[0]]  # new list starting with the first element of newtax
    for i in range(1, len(newtax)):
        tax_per_amount.append(newtax[i] - newtax[i-1])  # essentially: subtract the new tax from the previous, append.
    return tax_per_amount


def main():
    # It's possible to do this with a bunch of if statements, however, good programmers always think ahead:
    # If the taxes change or there's a new tax implemented, all we have to do to "fix" this code is add or change
    # one simple number.
    income = float(input("Income: "))
    newtax = [50_000, 75_000, 100_000, 250_000, 500_000]  # underscores are ignored -> use for better readability
    taxes = 0

    to_tax = income

    tax_percent = 0.00
    for tax_amount in tax_divider(newtax):
        tax_percent += 0.01

        if tax_amount <= to_tax:
            taxes += tax_amount * tax_percent
            to_tax -= tax_amount
        else:
            taxes += to_tax * tax_percent
            to_tax = 0
            break

    if to_tax > 0:
        taxes += to_tax * tax_percent

    print("Op $ {:.2f} dien je  $ {:.2f} inkomsbelastingen te betalen.".format(income, taxes))


main()
