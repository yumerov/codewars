# https://www.codewars.com/kata/find-the-unique-number-1/train/python

from unittest import TestCase

def find_uniq(arr):
    return list(filter(lambda x: arr.count(x) == 1, set(arr)))[0] or 0

test = TestCase()
test.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
test.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
test.assertEqual(find_uniq([ 3, 10, 3, 3, 3 ]), 10)