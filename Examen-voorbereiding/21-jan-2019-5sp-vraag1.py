# Note: there's probably a good package for making a grid element that would make this program way easier to read/write
# Regardless, gotta work with the knowledge we have, since we can't go online (or even on a computer).

# Combining the Dutch tasks and my English programming makes this a little messy. You have been warned.
# Add onto that the fact that I only slept 5 hours, well... just deal with it.

from random import choice


def check_grid_coordinates(rooster, positie):
    """
    An attempt at a workaround to writing "rooster[positie[0]][positie[1]]", because I feel like that's hard to read
    and also simply annoying. Would've preferred a way to write rooster[positie] or rooster[*positie]
    :param rooster: the grid, an n x m matrix.
    :param positie: a vector, pointing towards the position in the grid we're interested in.
    :return: The value of the grid at the given coordinates
    """
    return rooster[positie[0]][positie[1]]


def move_coordinates(positie, move):
    """
    Move a position vector by the given displacement vector, essentially adding the two vectors.
    :param positie: tuple or list, containing the coordinates of a vector
    :param move: tuple or list, containing the coordinates of a vector
    :return: a list of the new coordinates
    """
    if len(positie) != len(move):  # Just to make sure: check if they do in fact have the same dimensions
        raise ValueError("position and displacement vector dimensions are not equal")
    return [positie[i] + move[i] for i in range(len(positie))]


def move_robot(rooster, positie, orientatie, wall_following):
    """
    Moves the robot's position in the grid according to its position and orientation, and the wall it is supposed to
    follow.
    :param rooster: the grid
    :param positie: vector
    :param orientatie: digit, indicating the direction the robot is looking in
    :param wall_following: the wall that the robot is supposed to follow
    :return: the new position and direction the robot is looking in.
    """
    orientatie += wall_following
    orientatie %= 4

    VECTORIFY = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}  # constants, per convention, use uppercase
    # Not sure if this is also considered a "constant" though. Whatever. I consider it one.

    for i in range(4):
        new_position = move_coordinates(positie, VECTORIFY[orientatie])
        if check_grid_coordinates(rooster, new_position) in (1, 2):
            positie = new_position
            break
        orientatie -= wall_following
        orientatie %= 4

    return positie, orientatie


def run_through_maze(rooster, positie, orientatie, stappen):
    stap = 0
    while not check_grid_coordinates(rooster, positie) == 2 and stap < stappen:
        # Since the maximum "random" values for running along the left and right walls aren't given, I just
        # pick which one I continue following every step.
        wall_following = choice((-1, 1))  # -1 stands for a turn to the left in this program, 1 for right
        positie, orientatie = move_robot(rooster, positie, orientatie, wall_following)
        stap += 1

    return positie[0], positie[1], stap, check_grid_coordinates(rooster, positie) == 2


def histogram(rooster, positie, orientatie):
    print("STP AMOUNT | AMOUNT SUCCEEDED")
    print("=" * 29)
    for i in range(0, 100):
        succeeded = 0
        for j in range(100):
            succeeded += run_through_maze(rooster, positie, orientatie, i + 1)[3]  # if at_red, returns True (== 1)

        print(f"STEPS: {i + 1:03d} | " + f"{'#' * int(succeeded // 10):10s}" + f" ({succeeded:03d})")


def example_run_robot():
    rooster = [[0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 2, 0],
               [0, 0, 1, 0, 1, 0],
               [0, 1, 1, 1, 1, 0],
               [0, 1, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0]]

    begin_positie = (1, 1)
    orientatie = 0  # comparable to oriented angle in unit circle: 0 for right, 1 for 90° turn to the left (down), ...
    # Reminder that the y-axis points down, not up, due to the way that nested lists handle indexes,
    # i.e. rooster[0][0] is the top left most element, while rooster[5][0] is bottom left.
    # This can be "fixed" by reversing the elements of the outer list, such that the last list becomes the first and
    # therefore element reversed_rooster[0][0] would be the bottom left most element.

    histogram(rooster, begin_positie, orientatie)


example_run_robot()
