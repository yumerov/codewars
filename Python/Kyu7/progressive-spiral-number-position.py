# hhttps://www.codewars.com/kata/progressive-spiral-number-position/train/python

from unittest import TestCase
from math import ceil, floor


def layers(n):
    return floor(ceil(n ** 0.5) / 2) + 1


test = TestCase()
test.assertEqual(layers(1),1)
test.assertEqual(layers(5),2)
test.assertEqual(layers(25),3)
test.assertEqual(layers(30),4)
test.assertEqual(layers(50),5)