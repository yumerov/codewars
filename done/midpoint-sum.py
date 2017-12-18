# https://www.codewars.com/kata/midpoint-sum/train/python

from unittest import TestCase


def midpoint_sum(ints):
    for border in range(1, len(ints) - 1):
        if sum(ints[:border]) == sum(ints[border + 1:]):
            return border


test = TestCase()
test.assertEqual(midpoint_sum([4,1,7,9,3,9]), 3, "[4,1,7,9,3,9] should return 3")
test.assertEqual(midpoint_sum([1,0,1]), 1, "[1,0,1] should equal 1")
test.assertEqual(midpoint_sum([9,0,1,2,3,4]), 2, "[9,0,1,2,3,4] should equal 2")
test.assertEqual(midpoint_sum([0,0,4,0]), 2, "[0,0,4,0] should equal 2")
test.assertEqual(midpoint_sum([-10,3,7,8,-6,-13,21]), 4, "[-10,3,7,8,-6,-13,21] should equal 4")
test.assertEqual(midpoint_sum([1,1,1,1,-5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), 52, "Large valid sequence: [1,1,1,1,-5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] should equal 52")

