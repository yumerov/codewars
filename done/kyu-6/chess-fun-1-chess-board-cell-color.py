# https://www.codewars.com/kata/chess-fun-number-1-chess-board-cell-color/train/python

class Cell(object):
    colors = {
        0: "black",
        1: "white",
    }
    def __init__(self, pos):
        self.column = "ABCDEFGH".index(pos[0]) + 1
        self.row = int(pos[1])
    def color(self):
        return self.colors[(self.row + self.column) % 2]

def chess_board_cell_color(cell1, cell2):
    return Cell(cell1).color() == Cell(cell2).color()


from unittest import TestCase

tests = [
    # [[cell1, cell2], expected],
    [["A1", "C3"], True],
    [["A1", "H3"], False],
    [["A1", "A2"], False],
]
test = TestCase()
for inp, exp in tests:
    test.assertEqual(chess_board_cell_color(*inp), exp)