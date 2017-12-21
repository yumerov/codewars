# https://www.codewars.com/kata/counting-inner-calls-in-an-unknown-function/train/python


class F(object):
    calls = 0

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        F.calls += 1
        return result


def count_calls(func, *args, **kwargs):
    func = F(func)
    return F.calls, func(*args, **kwargs)

# tests

import unittest


def add(a, b): return a + b
def add_ten(a): return add(a, 10)
def misc_fun(): return add(add_ten(3), add_ten(9))

class CountCallsTest(unittest.TestCase):

    def test(self):
        self.assertEqual(count_calls(add, 8, 12), (0, 20))
        self.assertEqual(count_calls(add_ten, 5), (1, 15))
        self.assertEqual(count_calls(misc_fun), (5, 32))

if __name__ == '__main__':
    unittest.main()
