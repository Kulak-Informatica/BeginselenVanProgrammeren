# --- EXTRA: This is the expansion on exercise 2. For the regular, see 2-bar_graph.py ---

# Given:
# * all inputs are positive numbers.
# * Largest number must be represented by VALUE STRING where VALUE and STRING are inputs

# -- Inputting values --
# starting off with the two extra inputs and simply implementing them where I wrote "*" and 40
symbol = input("Symbols for graph: ")  # type(symbol) = str
symbol_amount = int(input("Max amount of symbols: "))  # type(amount) = int

values = input("Series of numbers, separated using spaces\n?>  ")
values = values.split(" ")
values = [float(i) for i in values]

max_value = max(values)

# -- Printing the bars --
for value in values:
    print(int(value/max_value * symbol_amount) * symbol)
