# https://www.codewars.com/kata/geometry-a-1-locate-point-to-the-right-to-the-left-or-on-the-vector/train/python

def get_cross_product(a, b):
    ax, ay = a
    bx, by = b
    dx, dy = ax - bx, ay - by


def point_vs_vector(point, vector):
    angle1 = get_cross_product(*vector)
    angle2 = get_cross_product(vector[0], point)
    if angle1 == angle2: return 0
    elif angle1 < angle2: return -1
    else: return 1

# tests

import unittest


class VectorClassSimpleTest(unittest.TestCase):

    def setUp(self):
        self.vector = [[0, 0], [1, 1]]

    def test_left(self):
        self.assertEqual(point_vs_vector((0, 1,), self.vector), -1)

    def test_on_line(self):
        self.assertEqual(point_vs_vector((2, 2,), self.vector), 0)

    def test_right(self):
        self.assertEqual(point_vs_vector((2, 0,), self.vector), 1)


if __name__ == '__main__':
    unittest.main()
