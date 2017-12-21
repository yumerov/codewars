# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python

def with_same_digits(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


def next_bigger(n):
    b = int("".join(sorted(str(n), reverse=True)))
    for i in xrange(n + 1, b + 1):
        if with_same_digits(i, b):
            return i
    return -1


# tests

from unittest import TestCase


class NextBiggerTest(TestCase):
    def test_with_small(self):
        data = [
            (12, 21,),
            (513, 531,),
            (2017, 2071,),
            (414, 441,),
            (144, 414,),
        ]
        for a, b in data:
            self.assertEqual(next_bigger(a), b)

    def test_negative(self):
        self.assertEqual(next_bigger(9), -1)

    def test_with_big(self):
        self.assertEqual(next_bigger(123456789), 123456798)
