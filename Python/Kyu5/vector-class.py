# https://www.codewars.com/kata/vector-class/train/python

from operator import add, sub, mul


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def apply(self, op, other):
        return Vector(list(map(op, self.vector, other.vector)))

    def is_compatable(self, other):
        if len(self.vector) != len(other.vector):
            pass

    def add(self, other):
        self.is_compatable(other)
        return self.apply(add, other)

    def subtract(self, other):
        self.is_compatable(other)
        return self.apply(sub, other)

    def dot(self, other):
        self.is_compatable(other)
        return sum(self.apply(mul, other).vector)

    def norm(self):
        return sum([v ** 2 for v in self.vector]) ** 0.5

    def __eq__(self, other):
        self.is_compatable(other)
        return self.vector == other.vector

    def equals(self, other):
        return self == other

    def __str__(self): return "({})".format(
        ",".join([str(v) for v in self.vector]))

# tests

import unittest


class VectorClassSimpleTest(unittest.TestCase):
    def test_add(self):
        a = Vector([1, 2])
        b = Vector([3, 4])
        self.assertTrue(a.add(b) == Vector([4, 6]))

class VectorClassAdvancedTest(unittest.TestCase):
    def setUp(self):
        self.a = Vector([1, 2, 3])
        self.b = Vector([3, 4, 5])

    def test_add(self):
        self.assertTrue(self.a.add(self.b) == Vector([4, 6, 8]))

    def test_sub(self):
        self.assertTrue(self.a.subtract(self.b) == Vector([-2, -2, -2]))

    def test_dot(self):
        self.assertEqual(self.a.dot(self.b), 26)

    def test_norm(self):
        self.assertEqual(self.a.norm(), 14 ** 0.5)

if __name__ == '__main__':
    unittest.main()
