# https://www.codewars.com/kata/gauss-needs-help-sums-of-a-lot-of-numbers/train/python

from unittest import TestCase


def f(n):
    if type(n) != int or n <= 0:
        return None
    return n * (n + 1) / 2

test = TestCase()
test.assertEqual(f(1), 1)
test.assertEqual(f(100), 5050)