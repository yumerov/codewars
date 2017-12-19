# https://www.codewars.com/kata/plotting-points-on-a-grid/train/python


class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = {}
        self.grid = ""
        self.fill_grid()
        self.update_grid()

    def fill_grid(self, fill = "0"):
        for h in range(1, self.height + 1):
            self.data[h] = {}
            for w in range(1, self.width + 1):
                self.data[h][w] = fill

    def update_grid(self):
        s = []
        for h in range(1, self.height + 1):
            row = ""
            for w in range(1, self.width + 1):
                row += self.data[h][w]
            s.append(row)
        self.grid = "\n".join(s)

    def plot_point(self, x, y):
        self.data[y][x] = "X"
        self.update_grid()

    def __repr__(self):
        pass


from unittest import TestCase
test = TestCase()
g = Grid(10, 10)
test.assertEqual(g.grid, '0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000\n0000000000')