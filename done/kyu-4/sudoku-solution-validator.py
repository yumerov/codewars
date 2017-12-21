# https://www.codewars.com/kata/sudoku-solution-validator/train/python

import unittest


def is_valid(element):
    return len(set(element)) == 9


def valid_row(board, index):
    return is_valid(board[index])


def valid_column(board, index):
    column = [row[index] for row in board]
    return is_valid(column)


def valid_sector(board, row, column):
    r = row * 3
    c = column * 3
    sector = []
    for row in board[r:r + 3]:
        sector.extend(row[c:c + 3])
    return is_valid(sector)


def validSolution(board):
    for r in range(9):
        if not valid_row(board, r):
            return False

    for c in range(9):
        if not valid_column(board, c):
            return False

    for r in range(3):
        for c in range(3):
            if not valid_sector(board, r, c):
                return False
    return True


class IpValidationTest(unittest.TestCase):
    valid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    invalid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 0, 3, 4, 9],
               [1, 0, 0, 3, 4, 2, 5, 6, 0],
               [8, 5, 9, 7, 6, 1, 0, 2, 0],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 0, 1, 5, 3, 7, 2, 1, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 0, 0, 4, 8, 1, 1, 7, 9]]

    def test_row_valid(self):
        self.assertTrue(valid_row(self.valid, 0))

    def test_row_invalid(self):
        self.assertFalse(valid_row(self.invalid, 8))

    def test_column_valid(self):
        self.assertTrue(valid_column(self.valid, 0))

    def test_column_invalid(self):
        self.assertFalse(valid_column(self.invalid, 1))

    def test_sector_valid(self):
        self.assertTrue(valid_sector(self.valid, 0, 0))

    def test_sector_invalid(self):
        self.assertFalse(valid_sector(self.invalid, 2, 2))

    def test_full_valid(self):
        self.assertTrue(validSolution(self.valid))

    def test_full_invalid(self):
        self.assertFalse(validSolution(self.invalid))


if __name__ == '__main__':
    unittest.main()
