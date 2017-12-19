# http://www.codewars.com/kata/shifted-cycles/train/python

from itertools import cycle


def item(index, length, iterable):
    step = []

    if isinstance(iterable, cycle):
        for i in range(length):
            next(iterable)
        i = 1
        for a in iterable:
            step.append(a)
            if i + index == length:
                break
            i += 1
    else:
        for i in range(length):
            step.append(iterable[(i + index) % len(iterable)])

    return tuple(step)


def gen(length, iterable):
    index = 0
    while True:
        yield item(index, length, iterable)
        index += 1


# tests
from itertools import islice
from unittest import TestCase

test = TestCase()
def t(a, b): test.assertEqual(a, b)
L = range(3)
t(item(0, 1, L), (0,))
t(item(1, 1, L), (1,))
t(item(2, 1, L), (2,))
t(item(3, 1, L), (0,))

c = cycle([1, 2, 3, 1, 2, 1, 2])
t(item(0, 3, cycle(c)), (1, 2, 3,))
t(item(1, 3, cycle(c)), (2, 3, 1,))
t(item(2, 3, cycle(c)), (3, 1, 2,))
t(item(3, 3, cycle(c)), (1, 2, 1,))
t(item(4, 3, cycle(c)), (2, 1, 2,))

result = [(0,), (1,), (2,), (0,)]
t(list(islice(gen(1, L), 4)), result)

result = [(0, 1), (1, 2), (2, 0), (0, 1), (1, 2)]
t(list(islice(gen(2, L), 5)), result)
