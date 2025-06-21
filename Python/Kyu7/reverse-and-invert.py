# https://www.codewars.com/kata/reverse-and-invert/train/python

from unittest import TestCase


def transform(num):
    if not isinstance(num, int):
        return

    if num == 0:
        return 0

    return (-num // abs(num)) * int(str(abs(num))[::-1])


def reverse_invert(lst):
    integers = filter(lambda x: isinstance(x, int), lst)
    return list(map(transform, integers))


test = TestCase()
test.assertEqual(reverse_invert([1,2,3,4,5]), [-1,-2,-3,-4,-5])
test.assertEqual(reverse_invert([-10]), [1])
test.assertEqual(reverse_invert([-9,-18,99]), [9,81,-99])
test.assertEqual(reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]),[-1,-21,-78,24,-5])
test.assertEqual(reverse_invert([]), [])