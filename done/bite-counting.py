# https://www.codewars.com/kata/bit-counting/train/python
from unittest import TestCase


def countBits(n): return bin(n).count("1")


test = TestCase()
test.assertEqual(countBits(0), 0)
test.assertEqual(countBits(4), 1)
test.assertEqual(countBits(7), 3)
test.assertEqual(countBits(9), 2)
test.assertEqual(countBits(10), 2)