# -- importing necessary packages --
import numpy as np
import matplotlib.pyplot as plt
# from time import sleep


# a simple function which creates a grid to work with
def create_grid(row_count=10, col_count=10):
    return np.zeros((row_count, col_count))


# a simple functions which puts a glider on the grid
def add_glider(game_grid, row_i, col_i):
    # test to see if possible:
    row_c, col_c = game_grid.shape
    if row_i > row_c - 3 or col_i > col_c - 3:
        raise IndexError("glider out of game bounds")

    # all good, add a glider
    glider = np.array([[0, 1, 0],
                       [0, 0, 1],
                       [1, 1, 1]])
    game_grid[row_i:row_i+3, col_i:col_i+3] = glider
    return game_grid


# a function to show the grid
# sadly, you need to update a grid manually: to continue with the code you MUST close the shown image. The code will
# continue and will show you the next iteration after.
def show_grid(game_grid):
    print("Array grid:\n", game_grid, sep="")
    plt.imshow(grid, cmap="gray")
    plt.show()


# a function which takes a look at all the cells in a 3x3 area of a certain cell, and counts all live cells.
# this, sadly, includes the cell itself.
def neighbour_array_sum(game_grid, row_index, column_index):
    row_min = max(0, row_index - 1)
    column_min = max(0, column_index - 1)
    neighbour_array = game_grid[row_min:row_index + 2, column_min:column_index + 2]
    # print("Neighbour array:\n", neighbour_array, sep="")
    # calling sum() on a 2D array gives you a 1D array where all the elements on the same column get summed up.
    # calling sum() on that 1D array gives you the total sum of all elements in the array.
    # if the sum has a shape of (0, 1), which can happen when you call array[2:2, 2:3] for example,
    # sum(array) will give an int. Performing sum on it again gives you a TypeError.
    try:
        sum_ = sum(sum(neighbour_array))  # a trailing underscore is used to not override the name of the function "sum"
    except TypeError:
        sum_ = sum(neighbour_array)
    # print("sum:\n", sum_, sep="")
    return sum_


# updates the original grid using the count grid. The reason we use the original grid is so we can just leave
# cells with 2 neighbours be, as dead cells with 2 neighbours stay dead, and live cells with 2 stay alive.
def update_grid(game_grid, count_grid):
    for row_index, row in enumerate(count_grid):
        for column_index, neighbour_count in enumerate(row):
            if neighbour_count < 2 or neighbour_count > 3:
                game_grid[row_index, column_index] = 0
            elif neighbour_count == 3:
                game_grid[row_index, column_index] = 1
    return game_grid


# creates a count grid, which shows how many live neighbours each cell has, and updates the original grid using it.
def next_iteration(game_grid):
    count_grid = np.zeros(np.shape(game_grid))
    for row_index, row in enumerate(game_grid):
        for column_index, cell in enumerate(row):
            # take the sum of all surrounding cells, minus the cell itself.
            count_grid[row_index][column_index] = neighbour_array_sum(game_grid, row_index, column_index) - cell
    # print("count grid:\n", count_grid, sep="")
    return update_grid(game_grid, count_grid)


# if you run this file, this code will be run. If you import it, the functions will get defined, but this bit of code
# won't run.
if __name__ == "__main__":
    grid = create_grid(20, 20)
    grid = add_glider(grid, 0, 1)
    grid[8:9, 6:9] = [[1, 1, 1]]
    show_grid(grid)
    for i in range(30):
        array = next_iteration(grid)
        show_grid(grid)
