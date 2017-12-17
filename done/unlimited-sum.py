# https://www.codewars.com/kata/unlimited-sum/train/python

from unittest import TestCase
from functools import reduce as r


def to_int(n): return n if isinstance(n, int) else 0


def sum(*args):
    return r(lambda x, y: to_int(x) + to_int(y), args, 0)


test = TestCase()
test.assertEqual(sum(1, 2, 3), 6)
test.assertEqual(sum(1, "2", 3), 4)