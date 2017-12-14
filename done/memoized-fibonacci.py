# https://www.codewars.com/kata/memoized-fibonacci

from unittest import TestCase

fib = {
    0: 0,
    1: 1,
}


def fibonacci(n):
    if n not in fib.keys():
        fib[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return fib[n]


test = TestCase()
test.assertEqual(fibonacci(70), 190392490709135)
test.assertEqual(fibonacci(60), 1548008755920)
test.assertEqual(fibonacci(50), 12586269025)