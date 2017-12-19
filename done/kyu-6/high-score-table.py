# https://www.codewars.com/kata/high-score-table/train/python


class HighScoreTable:
    def __init__(self, size):
        self.size = size
        self.reset()

    def update(self, item):
        self.scores.append(item)
        self.scores.sort(reverse=True)
        if len(self.scores) > self.size:
            self.scores.pop()

    def reset(self):
        self.scores = []

from unittest import TestCase
test = TestCase()
def t(a, b):
    test.assertEqual(a, b)

highScoreTable = HighScoreTable(3)
t(highScoreTable.scores, [])

highScoreTable.update(10)
t(highScoreTable.scores, [10])

highScoreTable.update(8)
highScoreTable.update(12)
t(highScoreTable.scores, [12, 10, 8])

highScoreTable.update(5)
t(highScoreTable.scores, [12, 10, 8])

highScoreTable.update(10)
t(highScoreTable.scores, [12, 10, 10])

highScoreTable.update(10)
t(highScoreTable.scores, [12, 10, 10])

highScoreTable.update(20)
t(highScoreTable.scores, [20, 12, 10])

highScoreTable.update(20)
t(highScoreTable.scores, [20, 20, 12])

highScoreTable.update(20)
t(highScoreTable.scores, [20, 20, 20])

highScoreTable.reset()
t(highScoreTable.scores, [])