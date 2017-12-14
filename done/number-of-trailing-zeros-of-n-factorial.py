# https://www.codewars.com/kata/number-of-trailing-zeros-of-n/train/python

from unittest import TestCase

from math import log


def zeros(n):
    if n < 1:
        return 0
    upper = int(log(n, 5))
    powers = range(upper, 0, -1)
    return sum(list(map(lambda x: n // (5 ** x), powers)))


test = TestCase()
test.assertEqual(zeros(6), 1)
test.assertEqual(zeros(12), 2)
test.assertEqual(zeros(19), 3)
test.assertEqual(zeros(26), 6)
test.assertEqual(zeros(30), 7)
test.assertEqual(zeros(100), 24)
