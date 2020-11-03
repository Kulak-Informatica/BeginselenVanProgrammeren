# I could actually implement this into a Discord bot as a challenge.
# I'll add this comment here as a reminder.

# This code is shit and rushed. Please check out master branch for actual nice looking and working code. Thanks.

from random import randint


# First, I'm defining a function to generate the piles.
# We could make the result a dictionary, but I think a list might be easier
def generate_piles(pile_amount=5, max_pile_size=5):
    print("Generating piles...")
    piles = []
    for i in range(pile_amount):
        piles.append(randint(1, max_pile_size))  # each pile will have a random value between 1 and 5 default
    print("Generating complete!")
    return piles


def print_board(piles):
    # start with a line to indicate where the board starts, with length the max length of the strings below it
    print("-" * (max(15 + max(piles), 18)))

    # print every pile, by its index.
    for i in range(len(piles)):
        if piles[i] == 0:
            print(f"Pile {i+1} -=- (EMPTY)")
        else:
            print(f"Pile {i+1} -=- ({piles[i]})", "|" * piles[i])
    print("-" * (max(15 + max(piles), 18)))


def main():
    # The program should start with adjusting the settings and starting the game.

    # -- SETTINGS --
    # Generating the piles got its own function, makes it simpler.
    print("By default, we play with 5 piles with a maximum size of 5 each.")
    change_settings = input("Change these settings? [Y/N]\n> ")

    # - Amount and size of piles -+- Generating piles -
    if "y" in change_settings.lower():
        pile_amount = int(input("Amount of piles:\n>"))
        while not pile_amount > 0:
            pile_amount = int(input("Please insert a valid amount of piles:\n> "))
        pile_size = int(input("Maximum size of a pile:\n> "))
        while not pile_size > 0:
            pile_size = int(input("Please insert a valid size:\n> "))
        piles = generate_piles(pile_amount, pile_size)
        del pile_amount
        del pile_size
    else:
        piles = generate_piles()  # Since I've set default values, this will generate 5 piles with max size 5

    # - Player Amount -
    player_count = int(input("Will you play with [1] or [2] players?\n> "))
    player_vs_player = True
    if player_count == 1:
        player_vs_player = False
    del player_count

    # -- START THE GAME --

    # We start off by printing the board and asking for the first player's move:
    turn = randint(0, 1)
    print_board(piles)

    if player_vs_player:
        while max(piles) != 0:
            turn_player(turn, piles)
            turn = (turn+1) % 2
    else:
        while max(piles) != 0:
            if turn == 0:
                turn_computer(piles)
            else:
                turn_player(0, piles)
            turn = (turn + 1) % 2


def turn_player(turn, piles):
    # Pick a pile and take the matches
    picked_pile = int(input(f"Player {turn+1}, Pick a pile > "))
    while picked_pile not in range(1, len(piles) + 1) or piles[picked_pile-1] == 0:
        picked_pile = int(input("Pick a pile > "))

    picked_pile -= 1

    picked_amount = input("Amount to take > ")
    if picked_amount == "":
        piles[picked_pile] = 0
    else:
        while int(picked_amount) > piles[picked_pile]:
            picked_amount = input("Amount to take > ")
        piles[picked_pile] -= int(picked_amount)

    print_board(piles)
    print(f"Player {turn + 1} took {picked_amount if picked_amount != '' else 'all'} from pile {picked_pile + 1}")


def turn_computer(piles, expert=False):
    if not expert:
        picked_pile = randint(0, len(piles)-1)
        picked_amount = randint(1, max(piles))
        piles[picked_pile] -= picked_amount

        # will grab even from empty piles
        print_board(piles)
        print(f"Computer took {picked_amount} from pile {picked_pile + 1}")
    else:
        nim_sum = 0
        for pile in piles:
            nim_sum += nim_sum ^ pile
        pick = []
        for i in range(0, len(piles)):
            if piles[i] ^ nim_sum < piles[i]:
                pick = [i, (piles[i] ^ nim_sum) - piles[i]]
        piles[pick[0]] -= pick[1]  # will return error if pick is empty
        print(f"Computer took {pick[1]} from pile {pick[0] + 1}")


main()
