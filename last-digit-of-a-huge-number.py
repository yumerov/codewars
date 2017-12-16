# https://www.codewars.com/kata/last-digit-of-a-huge-number/train/python

from unittest import TestCase


def last_digit(lst):
    l = len(lst)
    if l == 0: return 1
    if l == 1: return lst[0]

    head = lst[0:l - 2]
    tail = [pow(lst[-2], lst[-1], 10)]
    return last_digit(head + tail)

test = TestCase()
test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]
for test_input, test_output in test_data:
    test.assertEqual(
        first=last_digit(test_input),
        second=test_output,
        msg="{} => {}".format(test_input, test_output)
        )