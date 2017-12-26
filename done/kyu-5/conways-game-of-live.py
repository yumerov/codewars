# https://www.codewars.com/kata/conways-game-of-life/train/python


def count_alive_neighbors(cells, row, column):
    height = len(cells)
    width = len(cells[0])
    diffs = [-1, 0, 1]
    alive_cells = 0
    for dr in diffs:
        for dc in diffs:
            r = row + dr
            c = column + dc
            if 0 <= r < height and 0 <= c < width:
                alive_cells += cells[r][c]
    alive_cells -= cells[row][column]
    return alive_cells


def next_gen(cells):
    next_gen_matrix = []
    for r in range(len(cells)):
        row = []
        for c in range(len(cells[r])):
            alive_cells = count_alive_neighbors(cells, r, c)
            if cells[r][c] == 1:
                row.append(int(alive_cells in [2, 3]))
            else:
                row.append(int(alive_cells == 3))

        next_gen_matrix.append(row)

    return next_gen_matrix


# tests
import unittest


class CountAliveNeighborsTest(unittest.TestCase):
    def setUp(self):
        self.cells = [
            [1, 1, 0, ],
            [0, 1, 1, ],
            [1, 0, 0, ],
        ]

    def test_count_alive_neighbors(self):
        self.assertEqual(count_alive_neighbors(self.cells, 0, 0), 2)
        self.assertEqual(count_alive_neighbors(self.cells, 0, 1), 3)
        self.assertEqual(count_alive_neighbors(self.cells, 0, 2), 3)
        self.assertEqual(count_alive_neighbors(self.cells, 1, 0), 4)
        self.assertEqual(count_alive_neighbors(self.cells, 1, 2), 2)
        self.assertEqual(count_alive_neighbors(self.cells, 2, 0), 1)
        self.assertEqual(count_alive_neighbors(self.cells, 2, 1), 3)
        self.assertEqual(count_alive_neighbors(self.cells, 2, 2), 2)

    def test_next_gen(self):
        actual = next_gen(self.cells)
        expected = [
            [1, 1, 1,],
            [0, 0, 1,],
            [0, 1, 0,],
        ]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
