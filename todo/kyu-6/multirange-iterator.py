# https://www.codewars.com/kata/multirange-iterator/train/python

from unittest import TestCase
from operator import mul
from functools import reduce

def m(args):
    return reduce(mul, args, 1)

def convert(index, params):
    r = []
    for i in range(0, len(params)):
        r.append((index // m(params[:i])) % params[i])
    return tuple(r)


def multiiter(*params):
    if len(params) == 1 and params[0] == 0:
        yield []

    limit = m(params)
    for i in range(0, limit):
        yield convert(i, params)


test = TestCase()
def t(a, b):
    test.assertEqual(a, b)

t(convert(0, (2, 3)), (0, 0,))
t(convert(1, (2, 3)), (0, 1,))
t(convert(2, (2, 3)), (0, 2,))
t(convert(3, (2, 3)), (1, 0,))
t(list(multiiter(0)), [])
t(list(multiiter(2)), [(0,), (1,)])

t(list(multiiter(2, 3)),
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), ])
t(list(multiiter(3, 2)),
    [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), ])
