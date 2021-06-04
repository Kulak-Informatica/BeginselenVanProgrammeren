# IT WORKS. IT FUCKING WORKS.
# uh-- I mean, of course it works!
import numpy as np
import matplotlib.pyplot as plt


class Grid:
    def __init__(self, row_count=10, col_count=10):
        self.grid: np.ndarray = np.zeros((row_count, col_count))
        self.iteration: int = 0

    def reset_grid(self, row_count, col_count):
        self.grid = np.zeros((row_count, col_count))
        self.iteration = 0

    def add_glider(self, row_i, col_i):
        # test to see if possible:
        row_c, col_c = self.grid.shape
        if row_i > row_c - 3 or col_i > col_c - 3:
            raise IndexError("glider out of game bounds")

        # all good, add a glider
        glider = np.array([[0, 1, 0],
                           [0, 0, 1],
                           [1, 1, 1]])
        self.grid[row_i:row_i + 3, col_i:col_i + 3] = glider

    def __repr__(self):
        return "Grid:\n" + str(self.grid) + "\nIteration: " + str(self.iteration)

    def neighbour_array_sum(self, row_index, col_index):
        row_min = max(0, row_index - 1)
        col_min = max(0, col_index - 1)
        neighbour_array = self.grid[row_min:row_index + 2, col_min:col_index + 2]
        # print("Neighbour array:\n", neighbour_array, sep="")
        # calling sum() on a 2D array gives you a 1D array where all the elements on the same column get summed up.
        # calling sum() on that 1D array gives you the total sum of all elements in the array.
        # if the sum has a shape of (0, 1), which can happen when you call array[2:2, 2:3] for example,
        # sum(array) will give an int. Performing sum on it again gives you a TypeError.
        try:
            sum_ = sum(sum(neighbour_array))
        except TypeError:
            sum_ = sum(neighbour_array)
        # print("sum:\n", sum_, sep="")
        return sum_

    def update_grid(self, count_grid):
        for row_index, row in enumerate(count_grid):
            for col_index, neighbour_count in enumerate(row):
                if neighbour_count < 2 or neighbour_count > 3:
                    self.grid[row_index, col_index] = 0
                elif neighbour_count == 3:
                    self.grid[row_index, col_index] = 1

    def next_iteration(self):
        count_grid = np.zeros(np.shape(self.grid))
        for row_index, row in enumerate(self.grid):
            for column_index, cell in enumerate(row):
                # take the sum of all surrounding cells, minus the cell itself.
                count_grid[row_index][column_index] = self.neighbour_array_sum(row_index, column_index) - cell
        # print("count grid:\n", count_grid, sep="")
        self.update_grid(count_grid)
        self.iteration += 1

    def plot(self):
        plt.imshow(self.grid, cmap="gray")
        plt.show()


if __name__ == "__main__":
    grid = Grid(10, 10)
    grid.add_glider(0, 1)
    print(grid)
    grid.plot()
    for i in range(30):
        grid.next_iteration()
        print(grid)
        grid.plot()
