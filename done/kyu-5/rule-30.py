# https://www.codewars.com/kata/rule-30/train/python


def get_neighbors(index, list_):
    left = list_[index - 1] if index > 0 else 0
    mid = list_[index]
    right = list_[index + 1] if index < len(list_) - 1 else 0

    return left, mid, right

def new_cell(left, middle, right):
    return int(left == 0 if middle == 1 else left + right == 1)


def rule30(list_, n):
    if n < 1:
        return list_
    list_.insert(0, 0)
    list_.append(0)
    next_gen = [new_cell(*get_neighbors(i, list_)) for i in range(len(list_))]

    return rule30(next_gen, n - 1)

# tests

import unittest


class Rule30Test(unittest.TestCase):

    def test_neighbors(self):
        self.assertEqual(get_neighbors(1, [1, 1, 0]), (1, 1, 0, ))
        self.assertEqual(get_neighbors(0, [1]), (0, 1, 0,))

    def test_simple_one_gen(self):
        self.assertEqual(rule30([1], 1), [1, 1, 1])

    def test_simple_two_gens(self):
        self.assertEqual(rule30([1], 2), [1, 1, 0, 0, 1])
if __name__ == '__main__':
    unittest.main()
