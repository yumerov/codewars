# https://www.codewars.com/kata/unique-in-order/train/python

from unittest import TestCase


def lstrip(iterable, char):
    if len(iterable) == 0:
        return []

    if char == iterable[0]:
        return lstrip(iterable[1:], char)

    return iterable


def unique_in_order(iterable):
    if len(iterable) == 0:
        return []

    head = iterable[0]
    body = lstrip(iterable, head)

    queue = [head]
    queue.extend(unique_in_order(body))

    return queue


test = TestCase()
test.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
test.assertEqual(unique_in_order([1, 1, 2, 2, 3, 3, 1, 1]), [1, 2, 3, 1])
