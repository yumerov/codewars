# https://www.codewars.com/kata/next-prime/train/python

from unittest import TestCase


def is_prime(n):
    if n == 1:
        return False

    upper_limit = int(n ** 0.5) + 1
    for i in range(2, upper_limit):
        if n % i == 0:
            return False

    return True


def nextPrime(n):
    while True:
        n += 1
        if is_prime(n):
            return n



test = TestCase()
test.assertEqual(nextPrime(0),2)
test.assertEqual(nextPrime(1),2)
test.assertEqual(nextPrime(2),3)
test.assertEqual(nextPrime(3),5)
test.assertEqual(nextPrime(13),17)
test.assertEqual(nextPrime(181),191)
test.assertEqual(nextPrime(911),919)