# https://www.codewars.com/kata/progressive-spiral-number-distance/train/python

from unittest import TestCase


def two_sum(numbers, target):
    l = len(numbers)
    for x in range(0, l - 1):
        for y in range(x + 1, l):
            if numbers[x] + numbers[y] == target:
                return [x, y]


test = TestCase()
test.assertEqual(sorted(two_sum([1, 2, 3], 4)), [0, 2])
test.assertEqual(sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])
test.assertEqual(sorted(two_sum([2, 2, 3], 4)), [0, 1])
