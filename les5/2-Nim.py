# I could actually implement this into a Discord bot as a challenge.
# I'll add this comment here as a reminder.

from random import randint


# First, I'm defining a function to generate the piles.
# We could make the result a dictionary, but I think a list might be easier
def generate_piles(pile_amount=5, max_pile_size=5):
    piles = []
    for i in range(pile_amount):
        piles.append(randint(1, max_pile_size))  # each pile will have a random value between 1 and 5 default
    return piles


def main():
    print("By default, we play with 5 piles with a maximum size of 5 each.")
    change_settings = input("Change these settings? [Y/N]\n> ")
    if "y" in change_settings.lower():
        pile_amount = int(input("Amount of piles:\n>"))
        while not pile_amount > 0:
            pile_amount = int(input("Please insert a valid amount of piles:\n>"))
        pile_size = int(input("Maximum size of a pile:\n>"))
        while not pile_size > 0:
            pile_size = int(input("Please insert a valid size:\n>"))
        print("Generating piles...")
        generate_piles(pile_amount, pile_size)
    else:
        print("Generating piles...")
        generate_piles()  # Since I've set default values, this will generate 5 piles with max size 5
    player_count = int(input("Will you play with [1] or [2] players?\n>"))
    player_vs_player = False
    if player_count == 2:
        player_vs_player = True

