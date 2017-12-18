# https://www.codewars.com/kata/exercise-in-summing/train/python

from unittest import TestCase


def get_count(n):
    count = 0
    l = len(str(n))
    for length in range(1, l):
        for index in range(0, l - length + 1):
            divider = int(str(n)[index:index+length])
            if divider == 0:
                continue
            if n % divider == 0:
                count += 1

    return count


test = TestCase()


def testing(actual, expected):
    test.assertEqual(actual, expected)


testing(get_count(123), 2)
testing(get_count(1230), 5)
testing(get_count(1), 0)
testing(get_count(1111111111), 25)
