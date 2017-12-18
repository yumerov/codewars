# https://www.codewars.com/kata/explosive-sum/train/python

from unittest import TestCase


def exp_sum_with_len(n, l):
    if l == 1 or l == n:
        return 1

    s = 0
    for length in range(2, l + 1):
        s += exp_sum_with_len(n,length)

    return s


def exp_sum(n):
    if n < 0:
        return 0

    s = 0
    for i in range(1, n + 1):
        s += exp_sum_with_len(n, i)

    return s


test = TestCase()
test.assertEqual(exp_sum(-1), 0)
test.assertEqual(exp_sum(0), 1)
test.assertEqual(exp_sum(1), 1)
test.assertEqual(exp_sum(2), 2)
test.assertEqual(exp_sum(3), 3)
test.assertEqual(exp_sum(4), 5)
test.assertEqual(exp_sum(5), 7)
test.assertEqual(exp_sum(10), 42)