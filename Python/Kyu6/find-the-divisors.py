# https://www.codewars.com/kata/find-the-divisors/train/python
from unittest import TestCase


def divisors(integer):
    limit = int(integer * 0.5) + 1
    is_divisor = lambda x: integer % x == 0
    return list(filter(is_divisor, range(2, limit))) or "{} is prime".format(integer)


test = TestCase()
test.assertEqual(divisors(15), [3, 5]);
test.assertEqual(divisors(12), [2, 3, 4, 6]);
test.assertEqual(divisors(13), "13 is prime");