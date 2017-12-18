# https://www.codewars.com/kata/exercise-in-summing/train/python

from unittest import TestCase


def generic_sum(values, n, cmp):
    if len(values) == 0 or n == 0:
        return 0

    l = len(values)
    if n > l:
        return sum(values)

    m = sum(values[:n])
    for index in range(1, l - n + 1):
        current = sum(values[index:index + n])
        if cmp(current, m):
            m = current

    return m


def minimum_sum(values, n):
    return generic_sum(sorted(values), n, lambda c, m: c < m)


def maximum_sum(values, n):
    return generic_sum(sorted(values), n, lambda c, m: c > m)


test = TestCase()
# v1 = [5, 4, 3, 2, 1]
# test.assertEqual(minimum_sum(v1, 2), 3)
# test.assertEqual(maximum_sum(v1, 3), 12)
#
# v2 = [15, 14, 13, 12, 11]
# test.assertEqual(minimum_sum(v2, 2), 23)
# test.assertEqual(maximum_sum(v2, 8), 65)

v3 = [-5, -1, -3, -4, -2]
test.assertEqual(minimum_sum(v3, 2), -9)