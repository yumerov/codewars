# https://www.codewars.com/kata/progressive-spiral-number-distance/train/python

from unittest import TestCase


def sum_of_digits(s):
    return sum(map(lambda x: int(x), s))


def left(s):
    return s[:len(s) // 2]


def right(s):
    l = len(s)
    return s[(l // 2) + (l % 2):]


def luck_check(string):
    return sum_of_digits(left(string)) == sum_of_digits(right(string))


test = TestCase()
test.assertEqual(left("003111"), "003")
test.assertEqual(right("003111"), "111")
test.assertEqual(luck_check("003111"), True)

test.assertEqual(left("813372"), "813")
test.assertEqual(right("813372"), "372")
test.assertEqual(luck_check("813372"), True)

test.assertEqual(left("17935"), "17")
test.assertEqual(right("17935"), "35")
test.assertEqual(luck_check("17935"), True)

test.assertEqual(left("56328116"), "5632")
test.assertEqual(right("56328116"), "8116")
test.assertEqual(luck_check("56328116"), True)
