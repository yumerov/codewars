# https://www.codewars.com/kata/progressive-spiral-number-distance/train/python

from unittest import TestCase
from math import ceil, floor


def distance(n):
    return 2 * (ceil(ceil(n ** 0.5) / 2) - 1)


test = TestCase()
test.assertEqual(distance(1), 0)
test.assertEqual(distance(5), 2)
test.assertEqual(distance(25), 4)
test.assertEqual(distance(30), 5)
test.assertEqual(distance(50), 7)
