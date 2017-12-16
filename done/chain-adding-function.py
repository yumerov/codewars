# https://www.codewars.com/kata/a-chain-adding-function/train/python

from unittest import TestCase

class Add(int):
    def __call__(self, value):
        return Add(self + value)

def add(n):
    return Add(n)

test = TestCase()
test.assertEqual(add(1), 1)
test.assertEqual(add(1)(2), 3)
test.assertEqual(add(1)(2)(3), 6)